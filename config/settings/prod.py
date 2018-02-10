import dj_database_url

from .common import *

DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = [
    '.appspot.com'
]

DATABASES = {'default': dj_database_url.config()}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
