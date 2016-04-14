from django.shortcuts import render, redirect
from django.utils import timezone, text
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
		form = AddBlogForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.created_date = timezone.now()
			post.published_date = timezone.now()
			post.slug = text.slugify(post.title)
			post.post_image = request.FILES['post_image']
			post.save()

			return redirect(
				'blog:blog', slug=post.slug,
				year=post.published_date.year)
		else:
			form = AddBlogForm(instance=post)
			return render(request, 'blog/add_post.html', {'form': form})

	def get(self, request):
		form = AddBlogForm()
		return render(request, 'blog/add_post.html', {'form': form})
