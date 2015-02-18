SOCIAL_AUTH_TWITTER_KEY = 'EGmxjE55yVQigPCPWoMqdRsNp'
SOCIAL_AUTH_TWITTER_SECRET = '9rnyiG5HRHH187hkaaCaSADHNP4tRAD4Ob7SZiCJb9lSbWw3Pg'

SUPERVISOR_USER = 'user'
SUPERVISOR_PASSWORD = '123'
SUPERVISOR_URI = 'http://'+SUPERVISOR_USER+':'+SUPERVISOR_PASSWORD+'@127.0.0.1:9001'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tweetset',
        'USER': 'tweetset',
        'PASSWORD': 'somepassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
