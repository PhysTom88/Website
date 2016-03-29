from django.shortcuts import render

from .models import TextDescription

def home(request):
	message = TextDescription.objects.get(block_name='welcome')
	return render(request, 'home.html', {'message': message})


def about(request):
	return render_to_response(template_name='about.html')


def blog(request):
	return render_to_response(template_name='blog.html')


def photography(request):
	return render_to_response(template_name='photography.html')


def trips(request):
	return render_to_response(template_name='trips.html')
