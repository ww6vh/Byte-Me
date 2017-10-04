from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Computer, Review, User
import urllib.request, json

def index(request):
	template = loader.get_template('home.html')
	context = {}
	if request.method != 'GET':
		return HttpResponse(template.render(context, request))
	try:
		req = urllib.request.Request('http://exp-api:8000/api/v1/home')
	except e:
		return HttpResponse(template.render(context, request))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	context = resp["resp"]
	return HttpResponse(template.render(context, request))


def detail(request, computer_id):
	req = urllib.request.Request('http://exp-api:8000/exp/v2/computer/' + computer_id + '/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	#computer = get_object_or_404(Computer, pk=computer_id)
	return render(request, 'detail.html', resp)

