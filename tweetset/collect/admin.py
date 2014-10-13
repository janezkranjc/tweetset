from django.contrib import admin

from collect.models import Collection, Tweet
from django.db.models import Count

def start_collections(modeladmin, request, queryset):
    for c in queryset:
        c.start()
start_collections.short_description = "Start selected collections"

def stop_collections(modeladmin, request, queryset):
    for c in queryset:
        c.stop()
stop_collections.short_description = "Stop selected collections"

def empty_collections(modeladmin, request, queryset):
    for c in queryset:
        c.tweets.all().delete()
empty_collections.short_description = "Remove all tweets from selected collections"

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name','is_running','exists','user','tweetcount')
    raw_id_fields = ('user',)

    def get_queryset(self,request):
        return super(CollectionAdmin,self).get_queryset(request).annotate(tweetcount=Count('tweets'))

    def is_running(self,obj):
        return obj.is_running()

    def exists(self,obj):
        return obj.exists()

    def tweetcount(self,obj):
        return obj.tweetcount

    is_running.boolean = True
    exists.boolean = True
    actions = [start_collections,stop_collections,empty_collections]

class TweetAdmin(admin.ModelAdmin):
    list_display = ('twitter_id','text','collection')
    raw_id_fields = ('collection',)

    def text(self,obj):
        return obj.data['text']

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Tweet,TweetAdmin)
