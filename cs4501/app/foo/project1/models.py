from django.db import models

# Create your models here.

class Computer(models.Model):
	
	#Fields 
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	condition = models.CharField(max_length=10)
	description = models.CharField(max_length=500)

class User(models.Model):
	
	#Fields 
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	#Methods 
	def get_username(Self):
		return self.username

	def get_password(Self):
		return self.username

	def get_email(Self):
		return self.email

	def get_key(Self):
		return self.pk


class Review(models.Model):
	rating = models.IntegerField()
	description = models.CharField(max_length=500)









