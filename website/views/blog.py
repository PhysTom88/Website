from django.shortcuts import render
from django.views import generic

from website.models import BlogPost


class MainView(generic.View):

	def get(self, request, identifier=None):
		topics = map(lambda x: x[1], BlogPost.SUBJECT_CHOICE)
		years = map(lambda y: y.year,
				    BlogPost.objects.values_list('published_date')[0])

		if identifier in years:
			posts = (BlogPost.objects.filter(
				     published_date=int(identifier)).order_by('-published_date')[:6])
		elif identifier and identifier.upper() in topics:
			posts = (BlogPost.objects.filter(
				     subject=identifier).order_by('-published_date')[:6])
		else:
			posts = BlogPost.objects.all().order_by('-published_date')[:6]

		return render(request, 'blog/blog_main.html',
					  {'posts': posts, 'topics': topics, 'years': years})


class BlogPostView(generic.View):

	def get(self, request, slug, year):
		return render(request, 'blog/blog_post.html')
