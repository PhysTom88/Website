from django.shortcuts import render

from .models import TextDescription

def home(request):
	message = TextDescription.objects.get(block_name='welcome')
	return render(request, 'home.html', {'message': message})


def about(request):
	return render(request, 'about.html')


def blog(request):
	return render(request, 'blog.html')


def photography(request):
	return render(request, 'photography.html')


def trips(request):
	return render(request, 'trips.html')
