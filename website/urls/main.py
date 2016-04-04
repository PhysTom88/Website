from django.conf.urls import url

from website.views import main

urlpatterns = [
	url(r'^$', main.HomeView.as_view(), name='main'),
	url(r'^about/$', main.AboutView.as_view(), name='about'),
	url(r'^edit/(?P<message>[-\w]+)$', main.EditView.as_view(), name='main-edit')
]