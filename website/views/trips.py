from django.shortcuts import render
from django.views import generic

class MainView(generic.View):

	def get(self, request):
		return render(request, 'trips/trip_main.html')
