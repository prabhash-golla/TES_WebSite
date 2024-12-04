from pathlib import Path
import os
# from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-1-+^lln7ejdv0x5iszhnz!o9fy(-vw=1czhq0ue@a@vhv=7^eb'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tesapp',
    'taggit',
    'crispy_forms',
    'users',
    'compressor',
]

TAGGIT_CASE_INSENSITIVE = True
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tes.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dw_abhi',
#         'USER': 'postgres',
#         'PASSWORD': 'Alock@123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# # }
#  DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#      }
# }


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / "db.sqlite3",
    },
}



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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
USE_TZ = True

LOGIN_URL = 'user:login'
LOGIN_REDIRECT_URL = 'photo:list'
LOGOUT_REDIRECT_URL = 'photo:list'
COMPRESS_ROOT = BASE_DIR / 'static'
COMPRESS_ENABLED = True
STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

# AZURE_ACCOUNT_NAME = 'tesabhi'
# AZURE_ACCOUNT_KEY = 'WgWPCG2YRxwpmCa2cAFex6G6ke9y+UF1dlZ+MYZZED0Bt0lrp5DCcyOw2kBUB/09eipC6ME9Ia4S+AStOrBZPA=='
# AZURE_CONTAINER = 'myfiles'
# AZURE_URL_EXPIRATION_SECS = 3600  # Optional: Set the URL expiration time in seconds



