from django.shortcuts import render
from django.views import generic


class MainView(generic.View):

	def get(self, request):
		return render(request, 'photos/photo_main.html')


class AlbumView(generic.View):

	def get(self, request):
		return render(request, 'photos/photo_album.html')


class PhotoView(generic.View):

	def get(self, request):
		return render(request, 'photos/photo_photo.html')
