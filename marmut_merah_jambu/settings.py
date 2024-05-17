"""
Django settings for marmut_merah_jambu project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-1ccxps6zihnzbaskmu&w68ms-#20-!32yenx_mclvpd3ys-mfx'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-1ccxps6zihnzbaskmu&w68ms-#20-!32yenx_mclvpd3ys-mfx')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(",") + ['localhost']
SUPABASE_DB_URL = os.environ.get("SUPABASE_DB_URL")
DJANGO_ENV = os.environ.get('DJANGO_ENV')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'playlist',
    'cru_registrasi',
    'crud_kelola_album_song',
    'royalti',
    'main',
    'kelola_podcast',
    'chart',
    'dashboard',
    'langganan_paket',
    'pencarian',
    'downloaded_songs'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'marmut_merah_jambu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
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

WSGI_APPLICATION = 'marmut_merah_jambu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         "NAME": "postgres",
#         "USER": "postgres.cucamuatyldtkvxripor",
#         "PASSWORD": "Basdat-7-marmut",
#         "HOST": "aws-0-ap-southeast-1.pooler.supabase.com",
#         "PORT": "5432",
#         "OPTIONS": {"options": "-c search_path=marmut"},
#     }
# }

# Check if the Supabase database URL is set
if SUPABASE_DB_URL:
    # Use the Supabase database configuration
    DATABASES = {
        "default": dj_database_url.config(
            default=SUPABASE_DB_URL + '?options=-c%20search_path%3Dmarmut',
            conn_max_age=600
        )
    }
else:
    # Use the SQLite database configuration for development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            "NAME": "postgres",
            "USER": "postgres.cucamuatyldtkvxripor",
            "PASSWORD": "Basdat-7-marmut",
            "HOST": "aws-0-ap-southeast-1.pooler.supabase.com",
            "PORT": "5432",
            "OPTIONS": {"options": "-c search_path=marmut"},
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = 'static/'
# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
