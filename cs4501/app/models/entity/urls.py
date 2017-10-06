"""foo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    

	url(r'^api/v1/computer/$', views.get_all_computer, name = "get_all_computer"),

	url(r'^api/v1/user/(?P<pk>[0-9]+)/$', views.get_user, name = "get_user"),
	url(r'^api/v1/computer/(?P<pk>[0-9]+)/$', views.get_computer, name = "get_computer"),
	url(r'^api/v1/review/(?P<pk>[0-9]+)/$', views.get_review, name = "get_review"),

	url(r'^api/v1/user/create/$', views.create_user, name = "create_user"),
	url(r'^api/v1/computer/create/$', views.create_computer, name = "create_computer"),
	url(r'^api/v1/review/create/$', views.create_review, name = "create_review"),

	url(r'^api/v1/user/delete/(?P<pk>[0-9]+)/$', views.delete_user, name = "delete_user"),
	url(r'^api/v1/computer/delete/(?P<pk>[0-9]+)/$', views.delete_computer, name = "delete_computer"),
	url(r'^api/v1/review/delete/(?P<pk>[0-9]+)/$', views.delete_review, name = "delete_review"),

]
