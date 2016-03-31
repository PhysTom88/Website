from django.shortcuts import render
from django.views import generic


class MainView(generic.View):

	def get(self, request):
		return render(request, 'blog/blog_main.html')


class BlogPost(generic.View):

	def get(self, request, slug):
		return render(request, 'blog/blog_post.html')
