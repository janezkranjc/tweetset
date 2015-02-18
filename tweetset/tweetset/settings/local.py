from .base import *
from .passwords import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'tweetset', 'tweetset.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG_TOOLBAR:
    INTERNAL_IPS = ('127.0.0.1',)
