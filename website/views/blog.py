from django.shortcuts import render
from django.views import generic

from website.models import BlogPost


class MainView(generic.View):

	def get(self, request):
		posts = BlogPost.objects.all().order_by('publised_date')[:6]
		return render(request, 'blog/blog_main.html',
					  {'posts': posts})


class BlogPostView(generic.View):

	def get(self, request, slug):
		return render(request, 'blog/blog_post.html')
