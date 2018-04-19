from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/users$', views.new),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^users/(?P<number>\d+)$', views.show),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<number>\d+)/destroy$', views.destroy),
    url(r'^update/(?P<number>\d+)$', views.update)  # This line has changed!
]
