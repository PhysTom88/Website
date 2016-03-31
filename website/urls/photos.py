from django.conf.urls import url

from website.views import photos

urlpatterns = [
	url(r'^$', photos.MainView.as_view(), name='photos-main'),
]