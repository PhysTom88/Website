from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone, text
from django.views import generic

from website.models import BlogPost
from website.forms.blog import AddBlogForm, EditBlogForm


class MainView(generic.View):
	
	TOPICS, YEARS = BlogPost.get_blog_filter_contents()

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
		topics, years = BlogPost.get_blog_filter_contents()
		post = get_object_or_404(BlogPost, slug=slug)
		return render(request, 'blog/blog_post.html',
				      {'post': post, 'topics': topics, 'years': years})


class AddPostView(generic.View):

	def post(self, request):
		form = AddBlogForm(request.POST, request.FILES)
		if form.is_valid():
			blog_post = form.save(commit=False)
			blog_post.created_date = timezone.now()
			blog_post.published_date = timezone.now()
			blog_post.slug = text.slugify(blog_post.title)
			blog_post.post_image = request.FILES['post_image']
			blog_post.save()

			return redirect(
				'blog:blog', slug=blog_post.slug,
				year=blog_post.published_date.year)
		else:
			return render(request, 'blog/add_post.html', {'form': form})

	def get(self, request):
		form = AddBlogForm()
		return render(request, 'blog/add_post.html', {'form': form})
