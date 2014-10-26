# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import collect.models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_auto_20141026_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='follow',
            field=models.TextField(blank=True, help_text=b'A comma separated list of user IDs, indicating the users to return statuses for in the stream. More information at https://dev.twitter.com/docs/streaming-apis/parameters#follow', null=True, verbose_name=b'List of User IDs to follow (separated with commas)', validators=[collect.models.list_of_ids]),
        ),
    ]
