from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^admin/$', views.admin, name='add_blog'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^blog/(?P<id>\d+)/$', views.blog, name='blog'),  # < 1
    #path('', views.main, name='office-main'),
    url(r'^room/', views.room, name='office-room'),
    url(r'^ind/', views.ind, name='admin-ind'),
]
