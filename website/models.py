from django.db import models
from django.utils import timezone


class TextDescription(models.Model):
	'''Model for large pieces of text'''

	block_name = models.CharField(max_length=250, unique=True)
	block_text = models.TextField('Text')
	mod_date = models.DateField(blank=True, null=True)
	text_location = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.block_name


class BlogPost(models.Model):
	'''Model for blog posts'''
	SUBJECT_CHOICE = (
		('TEST', 'Test'),
		)

	title = models.CharField(max_length=250, unique=True, blank=False)
	text = models.TextField('text')
	subject = models.CharField(max_length=250, choices=SUBJECT_CHOICE, blank=False, null=True)
	created_date = models.DateField(default=timezone.now)
	published_date = models.DateField(null=True)
	post_image = models.ImageField(upload_to='blog/images/', max_length=100,
								   blank=False, null=True)

	slug = models.SlugField(max_length=255, default=None, null=True)

	@classmethod
	def get_blog_filter_contents(cls):
		topics = map(lambda x: x[1], BlogPost.SUBJECT_CHOICE)
		years = map(lambda y: y.year,
				BlogPost.objects.values_list('published_date')[0])
		return topics, years

	def __unicode__(self):
		return self.title
