from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer, Review, User
from django.core import serializers
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world!")

def success_response(status, data):
	return JsonResponse({'status': status, 'data': data})


def get_all_computer(request):
	computers = Computer.objects.all()
	data = [obj.toJson() for obj in computers]
	return success_response(True, data)


@csrf_exempt
def get_user(request, pk):
	try:
		user_instance = User.objects.get(pk=pk)
	except User.DoesNotExist:
		raise Http404("User does not exist")

	if request.method == 'GET':
		data = user_instance.toJson()
		return success_response(True, data)

	elif request.method == 'POST':
		user_instance.username = request.POST.get('username', "")
		user_instance.password = request.POST.get('password', "")
		user_instance.email = request.POST.get('email', "")
		user_instance.save()
		return success_response(True, "Updated")


@csrf_exempt
def get_computer(request, pk):
	try:
		computer_instance = Computer.objects.get(pk=pk)
	except Computer.DoesNotExist:
		raise Http404("Computer does not exist")

	if request.method == 'GET':
		data = computer_instance.toJson()
		return success_response(True, data)

	elif request.method == 'POST':
		computer_instance.make = request.POST.get('make', "")
		computer_instance.model = request.POST.get('model', "")
		computer_instance.condition = request.POST.get('condition', "")
		computer_instance.description = request.POST.get('description', "")
		computer_instance.save()
		return success_response(True, "Updated")


@csrf_exempt
def get_review(request, pk):
	try:
		review_instance = Review.objects.get(pk=pk)
	except Review.DoesNotExist:
		raise Http404("Review does not exist")

	if request.method == 'GET':
		data = review_instance.toJson()
		return success_response(True, data)

	elif request.method == 'POST':
		review_instance = Review.objects.get(pk=pk)
		review_instance.rating = request.POST.get('rating', "")
		review_instance.description = request.POST.get('description', "")
		review_instance.save()
		return success_response(True, "Updated")

@csrf_exempt
def create_user(request):
	try:
		iUsername = request.POST["username"]
		iPassword = request.POST["password"]
		iEmail = request.POST["email"]
	except:
		raise Http404("Not all fields are filled out.")

	instance = User(username = iUsername, password = iPassword, email = iEmail)
	instance.save()
	return success_response(True, "New item added")

@csrf_exempt
def create_computer(request):
	try:
		iMake = request.POST["make"]
		iModel = request.POST["model"]
		iCondition = request.POST["condition"]
		iDescription = request.POST["description"]
	except:
		raise Http404("Not all fields are filled out.")

	#User.models.create(username = iUsername, password = iPassword, email = iEmail)
	instance = Computer(make = iMake, model = iModel, condition = iCondition, description = iDescription)
	instance.save()
	return success_response(True, "New item added")

@csrf_exempt
def create_review(request):
	try:
		iDescription = request.POST["description"]
		iRating = request.POST["rating"]
	except:
		raise Http404("Not all fields are filled out." )

	iDescription = request.POST["description"]
	iRating = request.POST["rating"]

	instance = Review(rating = iRating, description = iDescription)
	instance.save()
	return success_response(True, "New item added")


def delete_user(request, pk): 
	try:
		user_instance = User.objects.get(pk=pk)
	except User.DoesNotExist:
		raise Http404("User does not exist")
	user_instance.delete()
	return success_response(True, "Item deleted")


def delete_computer(request, pk): 
	try:
		computer_instance = User.objects.get(pk=pk)
	except Computer.DoesNotExist:
		raise Http404("Computer does not exist")
	computer_instance.delete()
	return success_response(True, "Item deleted")


def delete_review(request, pk): 
	try:
		review_instance = User.objects.get(pk=pk)
	except Review.DoesNotExist:
		raise Http404("Review does not exist")
	review_instance.delete()
	return success_response(True, "Item deleted")
