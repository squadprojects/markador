from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmark_user'),
    url(r'^$', views.bookmark_list, name='bookmark_list'),
    url(r'^(?P<bookmark_id>[0-9]+)/$', views.detail, name='bookmark_details'),        
]

