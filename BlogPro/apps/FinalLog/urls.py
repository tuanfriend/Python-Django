#This is URL from Login App

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^register$', views.regacc),
    url(r'^login$', views.logacc),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]