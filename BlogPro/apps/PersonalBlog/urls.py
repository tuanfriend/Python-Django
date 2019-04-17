#This is URL from Personal Blog App
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^blog$', views.blog),
]