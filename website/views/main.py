from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone, text
from django.views import generic

from website.models import TextDescription, BlogPost
from website.forms import TextDescriptionForm


class HomeView(generic.View):

	def get(self, request):
		message = get_object_or_404(
			TextDescription, block_name="Welcome")
		latest_blog = BlogPost.objects.last()
		latest_blog.slug = text.slugify(latest_blog.title)
		return render(request, 'main/home.html',
					  {'message': message, 'blog': latest_blog})


class AboutView(generic.View):

	def get(self, request):
		bio_text = get_object_or_404(
			TextDescription, block_name="Biography")
		return render(request, 'main/about.html',
					  {'message': bio_text})


class EditView(generic.View):

	def post(self, request, message):
		message = get_object_or_404(
			TextDescription, block_name=message)
		form = TextDescriptionForm(request.POST, instance=message)
		if form.is_valid():
			message = form.save(commit=False)
			message.mod_date = timezone.now()
			message.save()

		return redirect(message.text_location)

	def get(self, request, message):
		message = get_object_or_404(
			TextDescription, block_name=message)
		form = TextDescriptionForm(instance=message)
		return render(request, 'main/edit.html',
				      {'form': form, 'title': message.block_name})
