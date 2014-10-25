from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.utils import puts
from fabric.context_managers import shell_env

env.hosts = ['git@tweetset.com']

def deploy():
    "deploys the project to the server"
    with prefix('source /srv/django-envs/tweetset/bin/activate'):
        with shell_env(DJANGO_SETTINGS_MODULE='tweetset.settings.production'):
            with cd('/srv/django-projects/tweetset'):
                puts(magenta("[Pulling changes]"))
                run('git pull origin master')

                puts(magenta("[Installing packages]"))
                run('pip install -r requirements.txt')

            with cd('/srv/django-projects/tweetset/tweetset'):
                puts(magenta("[Migrating apps]"))
                run('python manage.py migrate --no-initial-data')

                puts(magenta("[Collecting static files]"))
                run('python manage.py collectstatic --noinput')

                puts(magenta("[Touching wsgi.py]"))
                run('touch /srv/django-projects/tweetset/tweetset/tweetset/wsgi.py')

