from django.contrib import admin

from .models import TextDescription, BlogPost

class DescriptionAdmin(admin.ModelAdmin):
	fieldsets = [
	('Title', {'fields': ['block_name']}),
	('Text', {'fields': ['block_text']}),
	('URL', {'fields': ['text_location']}),
	('Date Modified', {'fields': ['mod_date']})
	]
	list_display = ('block_name', 'mod_date')
	search_fields = ['block_name']


class BlogPostAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['title']}),
	(None, {'fields': ['text']}),
	('Date Information', {'fields': ['created_date', 'published_date']}),
	(None, {'fields': ['post_image']})
	]
	list_display = ('title', 'created_date', 'published_date')
	list_filter = ['published_date']
	search_fields = ['title']

admin.site.register(TextDescription, DescriptionAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
