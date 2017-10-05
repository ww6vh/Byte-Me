from django.db import models

# Create your models here.

class Computer(models.Model):
	
	#Fields 
	make = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	condition = models.CharField(max_length=10)
	description = models.CharField(max_length=500)

	#Methods
	def toJson(self):
		return dict(computer_id = self.id,
					make = self.make,
					model = self.model,
					condition = self.condition,
					description = self.description)

class User(models.Model):
	
	#Fields 
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	#Methods 
	def toJson(self):
		return dict(user_id = self.id,
					username = self.username,
					password = self.password,
					email = self.emial)


class Review(models.Model):
	rating = models.IntegerField()
	description = models.CharField(max_length=500)

	#Methods
	def toJson(self):
		return dict(review_id = self.id,
					rating = self.rating,
					description = self.description)









