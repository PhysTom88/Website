from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^photography/$', views.photography, name='photography'),
	url(r'^trips/$', views.trips, name='trips'),
]