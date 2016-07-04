from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mytrips$', views.mytrips, name="mytrips"),
	url(r'^addtrip/(?P<id>\d+)$', views.addtrip, name="addtrip"),
	url(r'^addtripload$', views.addtripload, name="addtripload"),
	url(r'^join/(?P<id>\d+)$', views.join, name="join"),
	url(r'^others/(?P<id>\d+)$', views.others, name="others"),
]
