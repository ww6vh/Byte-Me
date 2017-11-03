
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [

	url(r'^api/v1/computer/(?P<pk>[0-9]+)/$', views.get_computer, name = "get_computer"),
	url(r'^api/v1/computer/create/$', views.create_computer, name="create_computer"),
	url(r'^api/v1/computer/delete/(?P<pk>[0-9]+)/$', views.delete_computer, name="delete_computer"),
	url(r'^api/v1/computer/$', views.get_all_computer, name = "get_all_computer"),

	url(r'^api/v1/review/(?P<pk>[0-9]+)/$', views.get_review, name="get_review"),
	url(r'^api/v1/review/create/$', views.create_review, name="create_review"),
	url(r'^api/v1/review/delete/(?P<pk>[0-9]+)/$', views.delete_review, name="delete_review"),

	url(r'^api/v1/user/(?P<pk>[0-9]+)/$', views.get_user, name = "get_user"),
	url(r'^api/v1/user/create/$', views.create_user, name = "create_user"),
	url(r'^api/v1/user/delete/(?P<pk>[0-9]+)/$', views.delete_user, name = "delete_user"),
	url(r'^api/v1/user/authenticate/$', views.authenticate_user, name = "authenticate_user"),

	url(r'^api/v1/authenticator/check/$', views.check_authenticator, name = "check_authenticator"),
	url(r'^api/v1/authenticator/create/$', views.create_authenticator, name = "create_authenticator"),
	url(r'^api/v1/authenticator/delete/$', views.delete_authenticator, name = "delete_authenticator"),

]
