from .base import *

DEBUG = False

ALLOWED_HOSTS = ['tweetset.com','www.tweetset.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tweetset',
        'USER': 'tweetset',
        'PASSWORD': 'kuracpalac',
        'HOST': '',
        'PORT': '',
    }
}
