from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer, Review, User
from django.core import serializers
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def get_user(request, pk):
	user_instance = None
	if request.method == 'GET':
		try:
			user_instance=User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404("User does not exist")

	if request.method == 'POST':
		try:
			user_instance = User.objects.get(pk=pk)
			user_instance.username = request.POST.get('username', "")
			user_instance.password = request.POST.get('password', "")
			user_instance.email = request.POST.get('email', "")
			user_instance.save()
		except User.DoesNotExist:
			raise Http404("User does not exist")
	
	user_as_json = serializers.serialize('json', [user_instance, ])
	return HttpResponse(user_as_json, content_type='json')	


@csrf_exempt
def get_computer(request, pk):
	computer_instance = None
	if request.method == 'GET':
		try:
			computer_instance=Computer.objects.get(pk=pk)
		except Computer.DoesNotExist:
			raise Http404("Computer does not exist")

	if request.method == 'POST':
		try:
			computer_instance = Computer.objects.get(pk=pk)
			computer_instance.make = request.POST.get('make', "")
			computer_instance.model = request.POST.get('model', "")
			computer_instance.condition = request.POST.get('condition', "")
			computer_instance.description = request.POST.get('description', "")
			computer_instance.save()
		except Computer.DoesNotExist:
			raise Http404("Computer does not exist")
	computer_as_json = serializers.serialize('json', [computer_instance, ])

	return HttpResponse(computer_as_json, content_type='json')

@csrf_exempt
def get_review(request, pk):
	review_instance = None
	if request.method == 'GET':
		try:
			review_instance = Review.objects.get(pk=pk)
		except Review.DoesNotExist:
			raise Http404("Review does not exist")

	if request.method == 'POST':
		try:
			review_instance = Review.objects.get(pk=pk)
			review_instance.rating = request.POST.get('rating', "")
			review_instance.description = request.POST.get('description', "")
			review_instance.save()

		except Review.DoesNotExist:
			raise Http404("Review does not exist")
	review_as_json = serializers.serialize('json', [review_instance, ])

	return HttpResponse(review_as_json, content_type='json')

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

	instance_as_json = serializers.serialize('json', [instance,])
	return HttpResponse(instance_as_json)

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
	
	instance_as_json = serializers.serialize('json', [instance,])
	return HttpResponse(instance_as_json)

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

	instance_as_json = serializers.serialize('json', [instance,])
	return HttpResponse(instance_as_json)

def delete_user(request, pk): 
	try:
		user_instance = User.objects.get(pk=pk)
	except User.DoesNotExist:
		raise Http404("User does not exist")

	save = user_instance
	user_instance.delete()
	user_as_json = serializers.serialize('json', [user_instance,])

	return HttpResponse(user_as_json + " Deleted")

def delete_computer(request, pk): 
	try:
		computer_instance = User.objects.get(pk=pk)
	except Computer.DoesNotExist:
		raise Http404("Computer does not exist")

	save = computer_instance
	computer_instance.delete()
	computer_as_json = serializers.serialize('json', [computer_instance,])

	return HttpResponse(computer_as_json + " Deleted")

def delete_review(request, pk): 
	try:
		review_instance = User.objects.get(pk=pk)
	except Review.DoesNotExist:
		raise Http404("Review does not exist")

	save = review_instance
	review_instance.delete()
	review_as_json = serializers.serialize('json', [review_instance,])

	return HttpResponse(review_as_json + " Deleted")









	
