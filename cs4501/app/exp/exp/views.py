import urllib.request
import urllib.parse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404


modelsApi = 'http://models-api:8000/api/v1/'


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
    resp = post_request(modelsApi + "computer/create/", {
        "make": request.POST.get("make", ""),
        "model": request.POST.get("model", ""),
        "condition": request.POST.get("condition", ""),
        "description": request.POST.get("description", "")
    })
    return JsonResponse(resp)


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