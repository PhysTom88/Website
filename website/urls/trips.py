from django.conf.urls import url

from website.views import trips

urlpatterns = [
	url(r'^$', trips.MainView.as_view(), name='trips-main')
]