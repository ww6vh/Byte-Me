from django.contrib import admin
from .models import Computer, User, Review

admin.site.register(Computer)
admin.site.register(User)
admin.site.register(Review)