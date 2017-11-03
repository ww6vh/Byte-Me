from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core import serializers
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
import os
import hmac
from datetime import datetime
from django.conf import settings

def index(request):
    return HttpResponse("Hello, world!")

def success_response(status, data, code):
	return JsonResponse({'status': status, 'data': data}, status=code)


def get_all_computer(request):
	try:
		computers = Computer.objects.all()
	except Computer.DoesNotExist:
		return success_response(False, "No computer in stock", 404)
	if request.method == 'GET':
		data = [obj.toJson() for obj in computers]
		return success_response(True, data, 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def get_user(request, pk):
	try:
		user_instance = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return success_response(False, "User does not exist", 404)

	if request.method == 'GET':
		data = user_instance.toJson()
		return success_response(True, data, 200)

	elif request.method == 'POST':
		try:
			user_instance.username = request.POST.get('username', "")
			user_instance.password = request.POST.get('password', "")
			user_instance.email = request.POST.get('email', "")
		except:
			raise Http404("Not all fields are filled out.")
		user_instance.save()
		return success_response(True, "Updated", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def get_computer(request, pk):
	try:
		computer_instance = Computer.objects.get(pk=pk)
	except Computer.DoesNotExist:
		return success_response(False, "Computer does not exist", 404)

	if request.method == 'GET':
		data = computer_instance.toJson()
		return success_response(True, data, 200)

	elif request.method == 'POST':
		try:
			computer_instance.make = request.POST.get('make', "")
			computer_instance.model = request.POST.get('model', "")
			computer_instance.condition = request.POST.get('condition', "")
			computer_instance.description = request.POST.get('description', "")
		except:
			raise Http404("Not all fields are filled out.")
		computer_instance.save()
		return success_response(True, "Updated", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def get_review(request, pk):
	try:
		review_instance = Review.objects.get(pk=pk)
	except Review.DoesNotExist:
		return success_response(False, "Review does not exist", 404)

	if request.method == 'GET':
		data = review_instance.toJson()
		return success_response(True, data, 200)

	elif request.method == 'POST':
		try:
			review_instance = Review.objects.get(pk=pk)
			review_instance.rating = request.POST.get('rating', "")
			review_instance.description = request.POST.get('description', "")
		except:
			raise Http404("Not all fields are filled out.")
		review_instance.save()
		return success_response(True, "Updated", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        usernames = User.objects.filter(username=request.POST["username"])
        if usernames.count() != 0:
            return success_response(False, "Username already exists", 200)
        try:
            iUsername = request.POST["username"]
            iPassword = request.POST["password"]
            iEmail = request.POST["email"]
            instance = User(username=iUsername, password=make_password(iPassword), email=iEmail)
            instance.save()
        except:
            return success_response(False, "Not all fields are filled out", 200)

        auth_token = create_authenticator(instance)
        return success_response(True, "New item added", 200)
    else:
        return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def create_computer(request):
    if request.method == 'POST':
        try:
            authenticator = Authenticator.objects.get(authenticator=request.POST.get('auth_token', ''))
        except:
            return success_response(False, "Must log in to create new listing", 200)
        try:
            iMake = request.POST["make"]
            iModel = request.POST["model"]
            iCondition = request.POST["condition"]
            iDescription = request.POST["description"]
            instance = Computer(make=iMake, model=iModel, condition=iCondition, description=iDescription)
            instance.save()
            response = {}
            response["id"] = instance.pk
        except:
            return success_response(False, "could not create computer", 200)
        return success_response(True, response, 200)
    else:
        return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def create_review(request):
	if request.method == 'POST':
		try:
			iDescription = request.POST["description"]
			iRating = request.POST["rating"]
		except:
			raise Http404("Not all fields are filled out." )

		instance = Review(rating = iRating, description = iDescription)
		instance.save()
		return success_response(True, "New item added", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def delete_user(request, pk):
	if request.method == 'DELETE':
		try:
			user_instance = User.objects.get(pk=pk)
		except User.DoesNotExist:
			return success_response(False, "User does not exist", 404)
		user_instance.delete()
		return success_response(True, "Item deleted", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def delete_computer(request, pk):
	if request.method == 'DELETE':
		try:
			computer_instance = Computer.objects.get(pk=pk)
		except Computer.DoesNotExist:
			return success_response(False, "Computer does not exist", 404)
		computer_instance.delete()
		return success_response(True, "Item deleted", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def delete_review(request, pk):
	if request.method == 'DELETE':
		try:
			review_instance = Review.objects.get(pk=pk)
		except Review.DoesNotExist:
			return success_response(False, "Review does not exist", 404)
		review_instance.delete()
		return success_response(True, "Item deleted", 200)
	else:
		return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def create_authenticator(user):
    if Authenticator.objects.filter(user_id=user).exists():
        Authenticator.objects.filter(user_id=user).delete()
    auth_token = hmac.new(
        key=settings.SECRET_KEY.encode('utf-8'),
        msg=os.urandom(32),
        digestmod='sha256',
    ).hexdigest()

    instance = Authenticator(authenticator=auth_token, user_id=user, date_created=datetime.now())
    instance.save()
    return auth_token


@csrf_exempt
def delete_authenticator(request):
    if request.method == 'POST':
        auth_token = request.POST['auth_token']
        try:
            auth = Authenticator.objects.get(authenticator=auth_token)
            auth.delete()
        except:
            return success_response(False, "Authenticator does not exist", 404)
        return success_response(True, "Authenticator deleted", 200)
    else:
        return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def check_authenticator(request):
    if request.method == 'GET':
        auth_token = request.GET.get("auth_token", "")
        try:
            auth = Authenticator.objects.get(authenticator=auth_token)
        except:
            return success_response(False, "Authenticator does not exist", 404)
        return success_response(True, {"user_id": auth.user.id, "username": auth.user.username}, 200)
    else:
        return success_response(False, "Invalid HTTP request", 404)


@csrf_exempt
def authenticate_user(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            auth_token = create_authenticator(user)
            return success_response(True, {"auth_token": auth_token}, 200)
        else:
            return success_response(False, "Either username or password is invalid", 200)
    except:
        return success_response(False, "Either username or password is invalid", 200)
