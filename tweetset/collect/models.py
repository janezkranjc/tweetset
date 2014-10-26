# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
import xmlrpclib
from django.conf import settings
import os
from email.utils import parsedate
from datetime import datetime

from django.core.exceptions import ValidationError

def list_of_ids(value):
    ids = value.split(',')
    try:
        for i in ids:
            int(i.strip())
    except:
        raise ValidationError("Please enter a list of numerical IDs")


class Collection(models.Model):
    name = models.CharField(max_length=100,help_text="Select a label for your collection of tweets.")
    follow = models.TextField(blank=True,null=True,help_text="A comma separated list of user IDs, indicating the users to return statuses for in the stream. More information at https://dev.twitter.com/docs/streaming-apis/parameters#follow",verbose_name="List of User IDs to follow (separated with commas)",validators=[list_of_ids])
    track = models.TextField(blank=True,null=True,help_text="A comma separated list of keywords or phrases to track. Phrases of keywords are specified by a comma-separated list. More information at https://dev.twitter.com/docs/streaming-apis/parameters#track",verbose_name="List of keywords to track (separated with commas)")
    locations = models.TextField(blank=True,null=True,help_text="A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. On geolocated Tweets falling within the requested bounding boxes will be included—unlike the Search API, the user\'s location field is not used to filter tweets. Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first. For example: \"-122.75,36.8,-121.75,37.8\" will track all tweets from San Francisco. NOTE: Bounding boxes do not act as filters for other filter parameters. More information at https://dev.twitter.com/docs/streaming-apis/parameters#locations",verbose_name="List of coordinates")
    user = models.ForeignKey(User,related_name="collections")

    def start(self):
        s = xmlrpclib.ServerProxy(settings.SUPERVISOR_URI)
        if not self.exists():
            try:
                s.twiddler.addProgramToGroup('tweetset', 'collection'+str(self.pk), 
                {'command':settings.PYTHON_EXECUTABLE+' '+os.path.join(settings.PROJECT_DIR,'manage.py')+' stream '+str(self.pk),
                'autostart':'false', 
                'autorestart':'true', 
                'startsecs':'3'})
            except:
                return False
        if not self.is_running():
            try:
                s.supervisor.startProcess('tweetset:collection'+str(self.pk))
            except:
                return False
            return True
        return True

    def stop(self):
        s = xmlrpclib.ServerProxy(settings.SUPERVISOR_URI)
        if self.exists():
            if self.is_running():
                s.supervisor.stopProcess('tweetset:collection'+str(self.pk))
            s.twiddler.removeProcessFromGroup('tweetset','collection'+str(self.pk))

    def exists(self):
        s = xmlrpclib.ServerProxy(settings.SUPERVISOR_URI)
        try:
            l = s.supervisor.getAllProcessInfo()
        except:
            return False
        names = [x['name'] for x in l]
        if 'collection'+str(self.pk) in names:
            return True
        else:
            return False

    def is_running(self):
        if self.exists():
            s = xmlrpclib.ServerProxy(settings.SUPERVISOR_URI)
            p_info = s.supervisor.getProcessInfo('tweetset:collection'+str(self.pk))
            if p_info['statename']=='RUNNING':
                return True
            else:
                return False
        else:
            return False

    def delete(self):
        self.stop()
        super(Collection, self).delete()

    def __unicode__(self):
        return unicode(self.name)

class Tweet(models.Model):
    data = JSONField()
    twitter_id = models.CharField(max_length=100,db_index=True)
    collection = models.ForeignKey(Collection,related_name="tweets")

    def parse_datetime(self):
        return datetime(*(parsedate(self.data['created_at'])[:6]))        

    def __unicode__(self):
        return unicode(self.twitter_id)