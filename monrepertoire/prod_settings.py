from .settings import *
import dj_database_url

# debug turned off in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['contacteznous.herokuapp.com']
# Application definition
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

DATABASES['default'] = dj_database_url.config()
