from django.conf.urls import include, url
from django.contrib import admin
from chatting.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^chat/', include('chatting.urls')),
    url(r'^admin/', admin.site.urls),
]