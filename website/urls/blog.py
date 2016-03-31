from django.conf.urls import url

from website.views import blog

urlpatterns = [
	url(r'^$', blog.MainView.as_view(), name='blog-main'),
	url(r'^(?P<title>\w+)/$', blog.BlogPost.as_view(), name='blog'),
]