from django.http import JsonResponse
from django.shortcuts import render
from .models import Computer, Review, User

def index(request):
	return render(request, ‘home.html')
