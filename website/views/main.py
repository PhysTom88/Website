from django.shortcuts import render
from django.utils.text import slugify

from website.models import TextDescription, BlogPost

def home(request):
	message = TextDescription.objects.get(block_name='welcome')
	latest_blog = BlogPost.objects.last()
	latest_blog.slug = slugify(latest_blog.title)
	return render(request, 'main/home.html',
				  {'message': message, 'blog': latest_blog})


def about(request):
	bio_text = TextDescription.objects.get(block_name='Biography')
	return render(request, 'main/about.html', {'message': bio_text})
