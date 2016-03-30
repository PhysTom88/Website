from django.db import models
from django.utils import timezone


class TextDescription(models.Model):
	'''Model for large pieces of text'''

	block_name = models.CharField(max_length=250, unique=True)
	block_text = models.TextField('block of text')
	mod_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.block_name


class BlogPost(models.Model):
	'''Model for blog posts'''

	title = models.CharField(max_length=250, unique=True)
	text = models.TextField('blog text')
	created_date = models.DateField(default=timezone.now)
	published_date = models.DateField(blank=True, null=True)
	post_image = models.CharField(max_length=250)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title
