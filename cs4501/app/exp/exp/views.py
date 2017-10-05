import urllib.request
import urllib.parse
import json
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


def index(request):
    resp = get_request(modelsApi + "computer")

    if resp['status'] != True:
        computers = []
    else:
        if len(resp['data']) > 3:
            computers = resp['data'][-3:]
        else:
            computers = resp['data']
        #computers = resp["data"]
    return JsonResponse({"status": True, "data": {"computers": computers}})


def computer_detail(request, id):
    resp = get_request(modelsApi + 'computer/' + id + '/')
    if resp['status'] != True:
        computer = []
    else:
        computer = resp['data']
    return JsonResponse({"status": True, "data": {"computer": computer}})