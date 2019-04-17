from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.allshows),
    url(r'^addshow$', views.addshows),
    url(r'^addshowBt$', views.addshowsBt),
    url(r'^shows/(?P<id>[0-9]+)$', views.showDT),
    url(r'^shows/(?P<id>[0-9]+)/edit$', views.showedit),
    url(r'^update$', views.updatebt),
    url(r'^shows/(?P<id>[0-9]+)/delete$', views.deleteBt),
]