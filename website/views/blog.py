from datetime import date

from django.shortcuts import render
from django.views import generic

from website.models import BlogPost


class MainView(generic.View):

	def get(self, request):
		posts = BlogPost.objects.all().order_by('publised_date')[:6]
		topics = map(lambda x: x[1], BlogPost.SUBJECT_CHOICE)
		years = map(lambda y: y.year,
				    BlogPost.objects.values_list('published_date')[0])
		return render(request, 'blog/blog_main.html',
					  {'posts': posts, 'topics': topics, 'years': years})


class BlogPostView(generic.View):

	def get(self, request, slug):
		return render(request, 'blog/blog_post.html')
