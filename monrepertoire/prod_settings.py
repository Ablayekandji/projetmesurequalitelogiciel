from .settings import *
import dj_database_url

# debug turned off in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['contacteznous.herokuapp.com']
# Application definition
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
]