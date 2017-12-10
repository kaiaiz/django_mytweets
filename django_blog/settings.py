"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "application"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yanchaomin'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.31.202',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

#    'dashing',
#    'ckeditor',
    'simditor',
    'taggit',
#    'haystack',
    'debug_toolbar',
    #add paginator
    'el_pagination',
    'rest_framework',

    'blog',
    'about',
    #'about.apps.AboutConfig',
    'shop',
    'cart',
    'orders',
    'coupons',
    #restful
    'api',
]

INSTALLED_APPS += ['django_summernote',
                   'imagekit',
                   'xadmin',
                   'crispy_forms',
                   'reversion']

AUTH_USER_MODEL = "about.UserProfile"

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    'about.authentication.EmailAuthBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'assets/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    os.path.join(BASE_DIR, "static/dashing/"),

]

SITE_ID = 1


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#Dashing settings
#DASHING = {
#    'INSTALLED_WIDGETS': ('number', 'list', 'graph'),
#    'PERMISSION_CLASSES': (
#        'dashing.permission.IsAuthenticated',
#    )
#}

#SIMDITOR SETTINGS
SIMDITOR_UPLOAD_PATH = 'uploads/'
SIMDITOR_IMAGE_BACKEND = 'pillow'

SIMDITOR_TOOLBAR = [
    'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
    'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
    'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
    'markdown'
]

SIMDITOR_CONFIGS = {
    'toolbar': SIMDITOR_TOOLBAR,
    'upload': {
        'url': '/simditor/upload/',
        'fileKey': 'upload'
    }
}


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__)),
    }
}

#shop setting
CART_SESSION_ID = 'cart'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Email send
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'mopdouba@163.com'
EMAIL_HOST_PASSWORD = 'xxxx'
EMAIL_POST = 25
EMAIL_USE_TLS = True
EMAIl_FROM = "mopdouban@163.com"

#csripy_forms templates
CRISPY_TEMPLATE_PACK = "bootstrap"

#rest_framework
REST_FRAMWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permission.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permission.IsAdminUser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGIBATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2
}

#login
LOGIN_REDIRECT_URL = 'about/login'
LOGIN_URL = 'about/login'
