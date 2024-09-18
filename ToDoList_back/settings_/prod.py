import os
from .base import *
import dj_database_url
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost","127.0.0.1","*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ToDoList-prueba',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5433'
    }
} """
""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todolistdb_mr8s',
        'USER': 'diacrami',
        'PASSWORD': 'vHAnn8ubMoCrIoLkuxk7EObdjC4nEzjR',
        'HOST': 'localhost',
        'PORT': '5432'
    }
} """

# Parse database configuration from $DATABASE_URL
""" import dj_database_url """
# DATABASES['default'] =  dj_database_url.config()
#updated
#DATABASES = {'default': dj_database_url.config(default='postgresql://diacrami:vHAnn8ubMoCrIoLkuxk7EObdjC4nEzjR@dpg-crkq07m8ii6s73851ltg-a.virginia-postgres.render.com/todolistdb_mr8s')}
DATABASES = {'default': dj_database_url.config(default='postgresql://diacrami:vHAnn8ubMoCrIoLkuxk7EObdjC4nEzjR@dpg-crkq07m8ii6s73851ltg-a/todolistdb_mr8s')}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
STATIC_URL = '/static/'

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

