from django.contrib import admin

from collect.models import Collection, Tweet
from django.db.models import Count

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name','is_running','exists','user','tweetcount')

    def queryset(self,request):
        return super(CollectionAdmin,self).queryset(request).annotate(tweetcount=Count('tweets'))

    def is_running(self,obj):
        return obj.is_running()

    def exists(self,obj):
        return obj.exists()

    def tweetcount(self,obj):
        return obj.tweetcount

    is_running.boolean = True
    exists.boolean = True

class TweetAdmin(admin.ModelAdmin):
    list_display = ('twitter_id','text','collection')

    def text(self,obj):
        return obj.data['text']

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Tweet,TweetAdmin)
