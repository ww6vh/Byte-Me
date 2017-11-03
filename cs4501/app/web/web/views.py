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

loggedIn = False


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
            return render(request, 'signup.html', {'signup_form': form, 'message': "Not all fields are filled"})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'signup_form': form})


@csrf_exempt
def login(request):
    global loggedIn
    auth = request.COOKIES.get('auth_token', '')
    if auth:
        loggedIn = True
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            resp = post_request(expApi + 'user/login/', form.cleaned_data)
            if not resp or resp['status'] is False:
                return render(request, 'login.html', {'login_form': form, 'message': resp['data']})
            else:
                auth_token = resp['data']['auth_token']
                response = HttpResponseRedirect(reverse('home'))
                loggedIn = True
                response.set_cookie('auth_token', auth_token)
                return response
        else:
            return render(request, 'login.html', {'login_form': form, 'message': "Username or Password is invalid"})
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'login_form': form, 'auth_token': auth})


@csrf_exempt
def create_listing(request):
    auth_token = request.COOKIES.get('auth_token')
    if not auth_token:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
        form = CreateListingForm(request.POST)
        if form.is_valid():
            data = {
                "auth_token": str(auth_token),
                "make": form.cleaned_data["make"],
                "model": form.cleaned_data["model"],
                "condition": form.cleaned_data["condition"],
                "description": form.cleaned_data["description"]
            }
            resp = post_request(expApi + 'computer/create/', data)
            if not resp or resp['status'] is False:
                return render(request, 'createlisting.html', {'createlisting_form': form, 'message': resp['data'], 'auth_token': auth_token})
            else:
                response = HttpResponseRedirect(reverse('home'))
                return response
        else:
            return render(request, 'createlisting.html', {'createlisting_form': form, 'message': "Invalid information", 'auth_token': auth_token})

    if request.method == 'GET':
        form = CreateListingForm()
        return render(request, 'createlisting.html', {'createlisting_form': form, 'auth_token': auth_token})


@csrf_exempt
def logout(request):
    global loggedIn
    auth = request.COOKIES.get('auth_token')
    if not auth:
        return HttpResponseRedirect(reverse('login'))
    response = HttpResponseRedirect(reverse('home'))
    response.delete_cookie('auth_token')
    loggedIn = False
    return response


def index(request):
    global loggedIn
    resp = get_request(expApi + 'popular/')
    context = {}
    if resp['status'] is True:
        context['popular_computers'] = resp['data']['computers']
    auth_token = request.COOKIES.get('auth_token')
    if auth_token:
        context['message'] = "You are logged in"
        loggedIn = True
    context['loggedIn'] = loggedIn
    return render(request, 'home.html', context)


def computer_detail(request, computer_id):
    resp = get_request(expApi + 'computer/' + computer_id + '/')
    if len(resp['data']['computer']) < 1:
        return render(request, 'error.html')
    else:
        return render(request, 'detail.html', resp['data'])


def search(request):
    query = request.GET.get('query', '').strip()
    if not query:
        return render(request, 'search_result.html', {'results': [], 'query': query})
    resp = get_request(expApi + 'computer/search/?query=' + query)
    if resp['status']:
        return render(request, 'search_result.html', {'results': resp['data'], 'query': query})
    else:
        return render(request, 'search_result.html', {'results': [], 'query': query})
