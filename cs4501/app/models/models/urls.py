
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('entity.urls')),
    url(r'', include('entity.urls')),
]
