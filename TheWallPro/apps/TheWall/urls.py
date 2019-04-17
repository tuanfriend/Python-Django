from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^register$', views.regacc),
    url(r'^success$', views.successpg),
    url(r'^login$', views.logacc),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^postmess$', views.postmess),
    url(r'^postcomment$', views.postcm),
    url(r'^edit$', views.editu),
    url(r'^editbt/(?P<id>[0-9]+)$', views.btedit),
    url(r'^post/(?P<id>[0-9]+)$', views.usermessage),
    url(r'^deletemess/(?P<id>[0-9]+)$', views.delemessage),
    url(r'^postlike/(?P<id>[0-9]+)$', views.postlike),
]