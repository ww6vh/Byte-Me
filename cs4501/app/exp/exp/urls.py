from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/index/$', views.index, name='index'),
    url(r'^api/computer/(?P<id>[0-9]+)/$', views.computer_detail, name='computer_detail'),
]
