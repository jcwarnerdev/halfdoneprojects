"""
Django settings for halfdoneprojects project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import re
import environ
# import django-en
from pathlib import Path
from django.core.management.utils import get_random_secret_key

import logging

logger = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

logger.debug(f'starting app from {os.getcwd()}')

#load .env and generate a key automatically if one isn't already in .env
env = environ.Env()
environ.Env.read_env(f'{BASE_DIR}/halfdoneprojects/.env', overwrite=True)
if "DJANGO_SECRET_KEY" not in env:
    logger.debug(os.getcwd())
    print('generating key')
    key = get_random_secret_key()
    logger.debug('writing secret key to .env')
    with open(f'{BASE_DIR}/halfdoneprojects/.env', 'r') as f:
        e = f.read()
    e = re.sub(r'DJANGO_SECRET_KEY=.*', f'DJANGO_SECRET_KEY={key}', e)
    with open(f'{BASE_DIR}/halfdoneprojects/.env', 'w') as f:
        f.write(e)
    os.environ["DJANGO_SECRET_KEY"] = key
if 'DJANGO_DEBUG' not in env:
# if not len(env("DJANGO_DEBUG")):
    logger.debug('writing DJANGO_DEBUG to .env')
    print(os.getcwd())
    with open(f'{BASE_DIR}/halfdoneprojects/.env', 'r') as f:
        e = f.read()
    e = re.sub(r'DJANGO_DEBUG=.*', f'DJANGO_DEBUG=False', e)
    with open(f'{BASE_DIR}/halfdoneprojects/.env', 'w') as f:
        f.write(e)
    os.environ["DJANGO_DEBUG"] = 'False'

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"] 


# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = env("DJANGO_DEBUG")
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
print(f'DEBUG is on: {DEBUG}')

# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '170.187.148.159', 'www.halfdoneprojects.com', 'chickendoor.halfdoneprojects.com', 'halfdoneprojects.com']
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(' ')

INTERNAL_IPS = [
    '127.0.0.1',
    '170.187.148.159',
    '76.100.105.82',
]

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'RENDER_PANELS': True,
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'django_quill',
    'taggit',
    'storages',
    'home',
    'blog',
    # 'silk',
    # 'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'silk.middleware.SilkyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'silk.middleware.SilkyMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'halfdoneprojects.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.project_list_ctx',
                'home.context_processors.media_url',
                'home.context_processors.static_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'halfdoneprojects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_TZ = True

USE_S3 = os.getenv('USE_S3', 'False') == 'True'

if USE_S3:
    # aws settings
    AWS_S3_FILE_OVERWRITE = False
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'no-cache'} # {'CacheControl': 'max-age=86400'}
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'halfdoneprojects.storage_backends.StaticStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'halfdoneprojects.storage_backends.PublicMediaStorage'
else:
    STATIC_URL = '/staticfiles/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/mediafiles/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

    # STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    # if os.environ["DJANGO_DEBUG"]:
    #     STATICFILES_DIRS = [
    #         os.path.join(BASE_DIR, 'static')
    #     ]
    # else:
    #     print('static root not debug')
    #     STATIC_ROOT = os.path.join(BASE_DIR, 'static/')



# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# # https://whitenoise.evans.io/en/latest/
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # media files
# # https://docs.djangoproject.com/en/4.1/ref/settings/#media-url
# # https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-MEDIA_ROOT
# # https://docs.djangoproject.com/en/4.1/topics/files/

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SILKY_PYTHON_PROFILER = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
}