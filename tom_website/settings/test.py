from tom_website.settings.base import *

DEBUG=True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'db.sqlite3'
	}
}

MEDIA_ROOT = '/Users/Tom/Documents/Play/Projects/Django/media/'
