from .base import *

SECRET_KEY = 'django-insecure-zzxxbj6ifhnstn3$^^bng6s_05od(fr$23d2czl+8pi8m)nspe'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
