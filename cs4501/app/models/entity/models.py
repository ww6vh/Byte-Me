from django.db import models

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
					email = self.email)


class Computer(models.Model):
    #Fields
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    condition = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    #price = models.IntegerField(max_length=10)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    #Methods
    def toJson(self):
        return dict(computer_id = self.id,
                    make = self.make,
                    model = self.model,
                    condition = self.condition,
                    description = self.description)
                    #price = self.price,
                    #user_id = User.toJson(self.user_id))


class Review(models.Model):
	rating = models.IntegerField()
	description = models.CharField(max_length=500)

	#Methods
	def toJson(self):
		return dict(review_id = self.id,
					rating = self.rating,
					description = self.description)


class Authenticator(models.Model):
	authenticator = models.CharField(max_length=64, primary_key=True, blank=False)
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField()