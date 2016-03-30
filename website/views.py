from django.shortcuts import render

from .models import TextDescription, BlogPost

def home(request):
	message = TextDescription.objects.get(block_name='welcome')
	latest_blog = BlogPost.objects.last()
	return render(request, 'home.html',
				  {'message': message, 'blog': latest_blog})


def about(request):
	return render(request, 'about.html')


def blog(request, title):
	return render(request, 'blog.html')


def photography(request):
	return render(request, 'photography.html')


def trips(request):
	return render(request, 'trips.html')
