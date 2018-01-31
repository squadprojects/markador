from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<bookmark_id>[0-9]+)/$', views.detail, name='bookmark_details'),        
]
