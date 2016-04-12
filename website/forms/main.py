from django import forms

from website.models import TextDescription

class TextDescriptionForm(forms.ModelForm):

	class Meta:
		model = TextDescription
		fields = ('block_text',)