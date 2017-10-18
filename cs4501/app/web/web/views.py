from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import *
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


def signup(request):
    auth = request.COOKIES.get('auth_token')
    if auth:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                return render(request, 'signup.html', {'signup_form': form, 'message': "Your Passwords do not match"})
            resp = post_request(expApi + 'user/create/', form.cleaned_data)
            if not resp or resp['status'] is False:
                return render(request, 'signup.html', {'signup_form': form, 'message': resp['data']})
            else:
                try:
                    response = HttpResponseRedirect(reverse('home'))
                    return response
                except Exception as e:
                    return render(request, 'signup.html', {'signup_form': form, 'message': str(e)})
        else:
            return render(request, 'signup.html', {'signup_form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'signup_form': form})


@csrf_exempt
def login(request):
    auth = request.COOKIES.get('auth_token')
    if auth:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            resp = post_request(expApi + 'user/login/', form.cleaned_data)
            if resp['status'] is False:
                return render(request, 'login.html', {'login_form': form, 'message': resp['data']})
            else:
                auth_token = resp['data']['auth_token']
                next = HttpResponseRedirect(reverse('home'))
                next.set_cookie('auth_token', auth_token)
                return next
        else:
            return render(request, 'login.html', {'login_form': form, 'message': "Username or Password is invalid"})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'login_form': form})


@csrf_exempt
def logout(request):
    auth = request.COOKIES.get('auth_token')
    data = {'auth_token': auth}
    response = HttpResponseRedirect(reverse('home'))
    response.delete_cookie('auth_token')
    resp = post_request(expApi + 'user/logout/', data)
    return response


def index(request):
    resp = get_request(expApi + 'index')
    return render(request, 'home.html', resp['data'])


def computer_detail(request, computer_id):
    resp = get_request(expApi + 'computer/' + computer_id + '/')
    if len(resp['data']['computer']) < 1:
        return render(request, 'error.html')
    else:
        return render(request, 'detail.html', resp['data'])

