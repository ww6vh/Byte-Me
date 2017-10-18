from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
 	url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^computerdetail/(?P<computer_id>[0-9]+)/$', views.computer_detail, name='computer_detail_page'),

]
