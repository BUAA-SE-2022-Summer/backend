# <<<<<<< HEAD:backend0_1/backend0_1/settings.py
# """
# Django settings for backend0_1 project.
# 
# Generated by 'django-admin startproject' using Django 4.0.6.
# 
# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/topics/settings/
# 
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.0/ref/settings/
# """
# 
# from pathlib import Path
# 
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# 
# 
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
# 
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-khk7ke!e5=j7_*e^v!(r76itg9u6ppx@pmo!aspk=8(v5h2kq%'
# 
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# 
# ALLOWED_HOSTS = []
# 
# 
# # Application definition
# 
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'user.apps.UserConfig',
# ]
# 
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# 
# ROOT_URLCONF = 'backend0_1.urls'
# 
# TEMPLATES = [
#     {
#         'BACKEND': 'django.templates.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates']
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.templates.context_processors.debug',
#                 'django.templates.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
# 
# WSGI_APPLICATION = 'backend0_1.wsgi.application'
# 
# 
# # Database
# # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# 
# 
# # Password validation
# # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
# 
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
# 
# 
# # Internationalization
# # https://docs.djangoproject.com/en/4.0/topics/i18n/
# 
# LANGUAGE_CODE = 'en-us'
# 
# TIME_ZONE = 'UTC'
# 
# USE_I18N = True
# 
# USE_TZ = True
# 
# 
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/
# 
# STATIC_URL = 'static/'
# 
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
# 
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# =======
"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import configparser
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-khk7ke!e5=j7_*e^v!(r76itg9u6ppx@pmo!aspk=8(v5h2kq%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "123.57.69.30",
    "127.0.0.1",
    'testserver',
    "horik.cn",
    '*'
]


# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'project.apps.ProjectConfig',
    'prototype.apps.PrototypeConfig',
    'team',
    'file',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('123.57.69.30', 6379)],
        },
    },
}


ROOT_URLCONF = 'backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

cf = configparser.ConfigParser()
cf.read(BASE_DIR / 'Config' / 'django.conf')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_backend',
        'USER': cf.get('db', 'MYSQL_USER'),
        'PASSWORD': cf.get('db', 'MYSQL_PWD'),
        'HOST': cf.get('db', 'MYSQL_HOST'),
        'PORT': '3306',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 指定邮件后端
EMAIL_HOST = 'smtpdm.aliyun.com'  # 发邮件主机
EMAIL_PORT = 80  # 发邮件端口
EMAIL_HOST_USER = 'mobook@horik.cn'  # 授权的邮箱
EMAIL_HOST_PASSWORD = '2022LiverTeam'  # 邮箱授权时获得的密码，非注册登录密码
EMAIL_FROM = '墨书<mobook@horik.cn>'  # 发件人抬头
# EMAIL_INVITATION_URL = 'http://123.57.69.30/email'
EMAIL_INVITATION_URL = 'http://123.57.69.30/app/web/email'
ASGI_APPLICATION = 'backend.routing.application'
