from django.db import models


class TextDescription(models.Model):
	'''Model for large pieces of text'''

	block_name = models.CharField(max_length=250, unique=True)
	block_text = models.TextField('block of text')
	pub_date = models.DateField('date published')
	mod_date = models.DateField('date last modified')

	def __unicode__(self):
		return self.block_name
