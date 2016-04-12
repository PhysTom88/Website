from django import forms

from website.models import BlogPost

class AddBlogForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ('title', 'text', 'subject', 'post_image')


class EditBlogForm(AddBlogForm):

	class Meta:
		pass
