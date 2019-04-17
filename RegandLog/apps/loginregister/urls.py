from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.regacc),
    url(r'^success$', views.successpg),
    url(r'^login$', views.logacc),
    url(r'^logout$', views.logout),
]