"""
Django settings for proj1949 project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t0$e!d^bfn(33wpvve@+r0ojmyn=0)5n=9a7wy!&g62(w@%(95'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['1949-intermediateteam.nl','team.1949-intermediateteam.nl','3.98.122.222']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proj1949.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'proj1949.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.postgresql',   
        'NAME': 'football',   
        'USER': 'vampah',   
        'PASSWORD': 'Val32roseamp',   
        'HOST': 'valadbtutorial.cyilvjfcctn7.ca-central-1.rds.amazonaws.com',   
        'PORT': '5432',     
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

STATIC_URL = 'static/'

#specify static root folder in EC2
STATIC_ROOT = '/home/ec2-user/SOCCERWEBAPP/proj1949/projApp/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BROWSER = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

#### adding configuration for staging and production



# Staging-specific settings
# if os.getenv('MYAPP_ENV') == 'staging':
#     ALLOWED_HOSTS = ['1949.staging.com']
#     DATABASES = {   
#     'default': {   
#         'ENGINE': 'django.db.backends.postgresql',   
#         'NAME': 'footballstaging',   
#         'USER': 'vampah',   
#         'PASSWORD': 'Val32roseamp',   
#         'HOST': 'valadbtutorial.cyilvjfcctn7.ca-central-1.rds.amazonaws.com',   
#         'PORT': '5432',     
#     }   
# } 
#     # Other staging-specific settings...

# # Production-specific settings
# if os.getenv('MYAPP_ENV') == 'production':
#     ALLOWED_HOSTS = ['1949.intermediateteam.com']
#     DATABASES = {   
#     'default': {   
#         'ENGINE': 'django.db.backends.postgresql',   
#         'NAME': 'football',   
#         'USER': 'vampah',   
#         'PASSWORD': 'Val32roseamp',   
#         'HOST': 'valadbtutorial.cyilvjfcctn7.ca-central-1.rds.amazonaws.com',   
#         'PORT': '5432',     
#     }   
# } 
#     # Other production-specific settings...
