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
	try:
		computers = Computer.objects.all()
	except Computer.DoesNotExist:
		return success_response(False, "No computer in stock")
	if request.method == 'GET':
		data = [obj.toJson() for obj in computers]
		return success_response(True, data)
	else:
		return success_response(False, "Invalid HTTP request")


@csrf_exempt
def get_user(request, pk):
	try:
		user_instance = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return success_response(False, "User does not exist")

	if request.method == 'GET':
		data = user_instance.toJson()
		return success_response(True, data)

	elif request.method == 'POST':
		try:
			user_instance.username = request.POST.get('username', "")
			user_instance.password = request.POST.get('password', "")
			user_instance.email = request.POST.get('email', "")
		except:
			raise Http404("Not all fields are filled out.")
		user_instance.save()
		return success_response(True, "Updated")
	else:
		return success_response(False, "Invalid HTTP request")


@csrf_exempt
def get_computer(request, pk):
	try:
		computer_instance = Computer.objects.get(pk=pk)
	except Computer.DoesNotExist:
		#raise Http404("Computer does not exist")
		return success_response(False, "Computer does not exist")

	if request.method == 'GET':
		data = computer_instance.toJson()
		return success_response(True, data)

	elif request.method == 'POST':
		try:
			computer_instance.make = request.POST.get('make', "")
			computer_instance.model = request.POST.get('model', "")
			computer_instance.condition = request.POST.get('condition', "")
			computer_instance.description = request.POST.get('description', "")
		except:
			raise Http404("Not all fields are filled out.")
		computer_instance.save()
		return success_response(True, "Updated")
	else:
		return success_response(False, "Invalid HTTP request")


@csrf_exempt
def get_review(request, pk):
	try:
		review_instance = Review.objects.get(pk=pk)
	except Review.DoesNotExist:
		return success_response(False, "Review does not exist")

	if request.method == 'GET':
		data = review_instance.toJson()
		return success_response(True, data)

	elif request.method == 'POST':
		try:
			review_instance = Review.objects.get(pk=pk)
			review_instance.rating = request.POST.get('rating', "")
			review_instance.description = request.POST.get('description', "")
		except:
			raise Http404("Not all fields are filled out.")
		review_instance.save()
		return success_response(True, "Updated")
	else:
		return success_response(False, "Invalid HTTP request")

@csrf_exempt
def create_user(request):
	if request.method == 'POST':
		try:
			iUsername = request.POST["username"]
			iPassword = request.POST["password"]
			iEmail = request.POST["email"]
		except:
			raise Http404("Not all fields are filled out.")

		instance = User(username = iUsername, password = iPassword, email = iEmail)
		instance.save()
		return success_response(True, "New item added")
	else:
		return success_response(False, "Invalid HTTP request")

@csrf_exempt
def create_computer(request):
	if request.method == 'POST':
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
	else:
		return success_response(False, "Invalid HTTP request")

@csrf_exempt
def create_review(request):
	if request.method == 'POST':
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
	else:
		return success_response(False, "Invalid HTTP request")


def delete_user(request, pk):
	if request.method == 'DELETE':
		try:
			user_instance = User.objects.get(pk=pk)
		except User.DoesNotExist:
			return success_response(False, "User does not exist")
		user_instance.delete()
		return success_response(True, "Item deleted")
	else:
		return success_response(False, "Invalid HTTP request")


def delete_computer(request, pk):
	if request.method == 'DELETE':
		try:
			computer_instance = Computer.objects.get(pk=pk)
		except Computer.DoesNotExist:
			return success_response(False, "Computer does not exist")
		computer_instance.delete()
		return success_response(True, "Item deleted")
	else:
		return success_response(False, "Invalid HTTP request")


def delete_review(request, pk):
	if request.method == 'DELETE':
		try:
			review_instance = Review.objects.get(pk=pk)
		except Review.DoesNotExist:
			return success_response(False, "Review does not exist")
		review_instance.delete()
		return success_response(True, "Item deleted")
	else:
		return success_response(False, "Invalid HTTP request")

