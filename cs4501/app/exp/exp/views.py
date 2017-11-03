import urllib.request
import urllib.parse
import json
from kafka import KafkaProducer
from elasticsearch import Elasticsearch
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404


modelsApi = 'http://models-api:8000/api/v1/'
es = Elasticsearch(['es'])


def get_request(url):
    req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return resp


def post_request(url, post_data):
    post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request(url, data=post_encoded, method='POST')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    return resp


@csrf_exempt
def create_user(request):
    resp = post_request(modelsApi + "user/create/", {
        "username": request.POST.get("username", ""),
        "password": request.POST.get("password", ""),
        "email": request.POST.get("email", "")})
    return JsonResponse(resp)


@csrf_exempt
def create_computer(request):
    post_data = {
        "auth_token": request.POST.get("auth_token", ""),
        "make": request.POST.get("make", ""),
        "model": request.POST.get("model", ""),
        "condition": request.POST.get("condition", ""),
        "description": request.POST.get("description", "")
    }
    resp = post_request(modelsApi + "computer/create/", post_data)

    if resp["status"]:
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        computer = {
            'make': post_data["make"],
            'model': post_data["model"],
            'description': post_data["description"],
            'condition': post_data["condition"],
            'id': resp["data"]["id"]
        }
        producer.send('new-listings-topic', json.dumps(computer).encode('utf-8'))
    return JsonResponse(resp)


def search_computer(request):
   if request.method == 'GET':
        query = request.GET.get('query', '').strip()
        try:
            result = es.search(index='listing_index', body={'query': {'query_string': {'query': query}}, 'size': 10})
        except Exception as e:
            return JsonResponse({"status": False, "data": str(e)})
        results = []
        for item in result['hits']['hits']:
            results.append(item['_source'])
        return JsonResponse({"status": True, "data": results})
   else:
       return JsonResponse({"status": False, "data": "Must be a GET request"})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        resp = post_request(modelsApi + 'user/authenticate/', {
            "username": request.POST.get("username", ""),
            "password": request.POST.get("password", "")
        })
        return JsonResponse(resp)


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        resp = post_request(modelsApi + 'authenticator/delete/', {
            'auth_token': request.COOKIES.get("auth_token", "")
        })
        return JsonResponse(resp)
    else:
        return JsonResponse({'status': False, 'data': "POST only"})


def check_authenticator(request):
    resp = post_request(modelsApi + 'authenticator/check/', request.GET)
    return JsonResponse(resp)


def populer_computers(request):
    resp = get_request(modelsApi + "computer/")

    if resp['status'] != True:
        computers = []
    else:
        #computers = resp['data']
        if len(resp['data']) > 3:
            computers = resp['data'][-3:]
        else:
            computers = resp['data']
    return JsonResponse({"status": True, "data": {"computers": computers}})


def computer_detail(request, id):
    resp = get_request(modelsApi + 'computer/' + id + '/')
    if resp['status'] != True:
        computer = []
    else:
        computer = resp['data']
    return JsonResponse({"status": True, "data": {"computer": computer}})