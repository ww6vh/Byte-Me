from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
import urllib.request
import urllib.parse
import json

expApi = 'http://exp-api:8000/api/'


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
    resp = get_request(expApi + 'index')
    return render(request, 'home.html', resp['data'])
    #return HttpResponse("hellow world")


def computer_detail(request, computer_id):
	resp = get_request(expApi + 'computer/' + computer_id + '/')
	#computer = get_object_or_404(Computer, pk=computer_id)
	return render(request, 'detail.html', resp['data'])

