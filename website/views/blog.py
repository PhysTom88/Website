from django.shortcuts import render
from django.views import generic

from website.models import BlogPost
from website.forms.blog import AddBlogForm, EditBlogForm


class MainView(generic.View):
	TOPICS = map(lambda x: x[1], BlogPost.SUBJECT_CHOICE)
	YEARS = map(lambda y: y.year,
				BlogPost.objects.values_list('published_date')[0])

	def get(self, request, identifier=None):
		if identifier:
			posts = self.filter_by_identifier(identifier)
		else:
			posts = BlogPost.objects.all().order_by('-published_date')[:6]

		return render(request, 'blog/blog_main.html',
					  {'posts': posts, 'topics': self.TOPICS, 'years': self.YEARS})

	def filter_by_identifier(self, identifier):
		if identifier in self.TOPICS:
			posts = (BlogPost.objects.filter(
				     subject=identifier.upper()).order_by('-published_date'))
		else:
			posts = (BlogPost.objects.filter(
				     published_date__year=identifier).order_by('-published_date'))

		return posts


class BlogPostView(generic.View):

	def get(self, request, slug, year):
		return render(request, 'blog/blog_post.html')


class AddPostView(generic.View):

	def post(self, request):
		return

	def get(self, request):
		form = AddBlogForm()
		return render(request, 'blog/add_post.html', {'form': form})
