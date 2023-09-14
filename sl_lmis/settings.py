"""
Django settings for sl_lmis project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url
from decouple import config
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', default=False)

port = int(os.environ.get('PORT', 8000))

ENV_ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS') or None
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    #'jet.dashboard',
    #'jet',
    'jazzmin',
    #'admin_adminlte.apps.AdminAdminlteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'accounts.apps.AccountsConfig',
    'jobs.apps.JobsConfig',
    'news_and_events.apps.NewsAndEventsConfig',
    'crispy_forms',
    'crispy_bootstrap5',
    'phonenumber_field',
    'widget_tweaks',
    'django_bootstrap_icons',
    'lmi.apps.LmiConfig',
    'fontawesomefree',
    'career_dev.apps.CareerDevConfig',
    'training_programs.apps.TrainingProgramsConfig',
    'plotly',
    'ckeditor',
    'cloudinary_storage',
    'cloudinary',
    'resources.apps.ResourcesConfig',
    'taggit',
    'formtools',
] 

AUTH_USER_MODEL = 'accounts.User'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'sl_lmis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.jobseeker_id',
                'accounts.context_processors.employer_id',
            ],
        },
    },
]

WSGI_APPLICATION = 'sl_lmis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "sl_lmis",
            "USER": "root",
            "PASSWORD": "Yusuf290419#",
            "HOST": '127.0.0.1',
            "PORT": "3306"
        }
    }
else:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = '/images/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
django_heroku.settings(locals())

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/images'

if os.environ["ENVIRONMENT"] == "PRODUCTION":
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME' : os.environ['CLOUD_NAME'],
    'API_KEY' : os.environ['API_KEY'],
    'API_SECRET' : os.environ['API_SECRET']
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        "toolbar": "full",
        'height': 300,
        'width': '100%',
        "extraPlugins": ",".join(
            [
                'about',
                'filetools',
                'find',
                'iframe',
                'image',
                'image2',
                'link',
                'smiley',
                'table',
                'tabletools',
                'uploadimage',
                'widget',
                'dialog',
            ]
        ),
    }
}

AUTHENTICATION_BACKENDS = [
    'accounts.backends.CustomUserBackend',  # Replace with your actual authentication backend
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = "/"  # Set to None to use the custom authentication backend for redirection
#LOGIN_REDIRECT_URL = "/accounts/jobseeker_dashboard/"
# SMTP Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['HOST_USER'],
EMAIL_HOST_PASSWORD = os.environ['HOST_PASSWORD'],
DEFAULT_FROM_EMAIL = os.environ['EMAIL'],


LOGIN_URL = 'accounts:login'
LOGOUT_REDIRECT_URL = "/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
