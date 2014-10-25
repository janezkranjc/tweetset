from .base import *

DEBUG = False

ALLOWED_HOSTS = ['tweetset.com','www.tweetset.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tweetset',
        'USER': 'tweetset',
        'PASSWORD': 'kuracpalac',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = 'http://static.tweetset.com/'