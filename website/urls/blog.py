from django.conf.urls import url

from website.views import blog

urlpatterns = [
	url(r'^$', blog.MainView.as_view(), name='blog-main'),
	url(r'^(?P<slug>[-\w]+)/$', blog.BlogPostView.as_view(), name='blog'),
]