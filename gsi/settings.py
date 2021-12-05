"""
Django settings for gsi project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
import djongo

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-35xjl*0vkudar2)d1ah1%-d6fs$$d!o0tm*ys%f4@@brmu2(5p'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("ENV")=='PRODUCTION':
    DEBUG=False
else:
    DEBUG=True

ALLOWED_HOSTS = ['127.0.0.1','gsi.herokuapp.com','.gsi.herokuapp.com']

INTERNAL_IPS=[ '127.0.0.1'] #to change
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eptGSI.apps.EptgsiConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters'
    ]


DATE_INPUT_FORMATS = ['%d/%m/%Y']

REST_FRAMEWORK = {
    "DATE_INPUT_FORMATS": [("%Y-%m-%d")],

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', 
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':3
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'gsi.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'gsi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'gsi',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false'
            }  
        }
}


BASE_URL="http://127.0.0.1:8000/"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

UPLOADED_FILES_USE_URL = True

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


PROJECT_DIR = os.path.dirname(__file__) 
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

    # Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),    
    )
if os.environ.get('ENV') == 'PRODUCTION':
    # Simplified static file serving.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # https://warehouse.python.org/project/whitenoise/
    #STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

