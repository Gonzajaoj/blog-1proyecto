from .base import *
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'go987ja654oj321',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
