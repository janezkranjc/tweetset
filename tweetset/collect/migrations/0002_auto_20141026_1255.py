# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='follow',
            field=models.TextField(help_text=b'A comma separated list of user IDs, indicating the users to return statuses for in the stream. More information at https://dev.twitter.com/docs/streaming-apis/parameters#follow', null=True, verbose_name=b'List of User IDs to follow (separated with commas)', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='locations',
            field=models.TextField(help_text=b'A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. On geolocated Tweets falling within the requested bounding boxes will be included\xe2\x80\x94unlike the Search API, the user\'s location field is not used to filter tweets. Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first. For example: "-122.75,36.8,-121.75,37.8" will track all tweets from San Francisco. NOTE: Bounding boxes do not act as filters for other filter parameters. More information at https://dev.twitter.com/docs/streaming-apis/parameters#locations', null=True, verbose_name=b'List of coordinates', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='track',
            field=models.TextField(help_text=b'A comma separated list of keywords or phrases to track. Phrases of keywords are specified by a comma-separated list. More information at https://dev.twitter.com/docs/streaming-apis/parameters#track', null=True, verbose_name=b'List of keywords to track (separated with commas)', blank=True),
        ),
    ]
