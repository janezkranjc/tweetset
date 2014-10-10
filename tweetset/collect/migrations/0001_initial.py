# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('follow', models.TextField(help_text=b'A comma separated list of user IDs, indicating the users to return statuses for in the stream. More information at https://dev.twitter.com/docs/streaming-apis/parameters#follow', null=True, blank=True)),
                ('track', models.TextField(help_text=b'A comma separated list of keywords or phrases to track. Phrases of keywords are specified by a comma-separated list. More information at https://dev.twitter.com/docs/streaming-apis/parameters#track', null=True, blank=True)),
                ('locations', models.TextField(help_text=b'A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. On geolocated Tweets falling within the requested bounding boxes will be included\xe2\x80\x94unlike the Search API, the user\'s location field is not used to filter tweets. Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first. For example: "-122.75,36.8,-121.75,37.8" will track all tweets from San Francisco. NOTE: Bounding boxes do not act as filters for other filter parameters. More information at https://dev.twitter.com/docs/streaming-apis/parameters#locations', null=True, blank=True)),
                ('firehose', models.BooleanField(default=False, help_text=b'Use this option to receive all public tweets if there are no keywords, users or locations to track. This requires special permission from Twitter. Otherwise a sample of 1 percent of tweets will be returned.')),
                ('consumer_key', models.TextField(help_text=b'The consumer key that you obtain when you create an app at https://apps.twitter.com/', max_length=150)),
                ('consumer_secret', models.TextField(help_text=b'The consumer secret that you obtain when you create an app at https://apps.twitter.com/', max_length=150)),
                ('access_token', models.TextField(help_text=b"You can generate your user access token at http://apps.twitter.com by clicking 'Create my access token'.", max_length=150)),
                ('access_token_secret', models.TextField(help_text=b"You can generate your user access token secret at http://apps.twitter.com by clicking 'Create my access token'.", max_length=150)),
                ('user', models.ForeignKey(related_name=b'collections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', jsonfield.fields.JSONField()),
                ('twitter_id', models.CharField(max_length=100, db_index=True)),
                ('collection', models.ForeignKey(related_name=b'tweets', to='collect.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
