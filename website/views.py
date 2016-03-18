from django.shortcuts import render_to_response

def home(request):
	return render_to_response(template_name='home.html')


def about(request):
	return render_to_response(template_name='about.html')


def blog(request):
	return render_to_response(template_name='blog.html')


def photography(request):
	return render_to_response(template_name='photography.html')


def trips(request):
	return render_to_response(template_name='trips.html')
