from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/popular/$', views.populer_computers, name='popular_computers'),
    url(r'^api/computer/(?P<id>[0-9]+)/$', views.computer_detail, name='computer_detail'),
    url(r'^api/computer/create/$', views.create_computer, name='create_computer'),
    url(r'^api/user/create/$', views.create_user, name='create_user'),
    url(r'^api/user/login/$', views.login, name='login'),
    url(r'^api/user/logout/$', views.logout, name='logout'),
    url(r'^api/authenticator/check/$', views.check_authenticator, name='check_authenticator'),
    url(r'^api/computer/search/', views.search_computer, name='search_computer'),
]
