from django.shortcuts import render, redirect
from django.utils import timezone, text

from website.models import TextDescription, BlogPost
from website.forms import TextDescriptionForm

def home(request):
	message = TextDescription.objects.get(block_name='welcome')
	latest_blog = BlogPost.objects.last()
	latest_blog.slug = text.slugify(latest_blog.title)
	return render(request, 'main/home.html',
				  {'message': message, 'blog': latest_blog})


def about(request):
	bio_text = TextDescription.objects.get(block_name='Biography')
	return render(request, 'main/about.html', {'message': bio_text})


def edit(request):
	message = TextDescription.objects.get(block_name='welcome')
	if request.method == 'POST':
		form = TextDescriptionForm(request.POST, instance=message)
		if form.is_valid():
			message = form.save(commit=False)
			message.mod_date = timezone.now()
			message.save()
			return redirect('main:main')
	else:
		form = TextDescriptionForm(instance=message)
	return render(request, 'main/edit.html', {'form': form, 'title': message.block_name})
