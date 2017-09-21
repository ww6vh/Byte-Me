from django.contrib import admin
from .models import Computer, User, Review

# Register your models here.
admin.site.register(Computer)
admin.site.register(User)
admin.site.register(Review)