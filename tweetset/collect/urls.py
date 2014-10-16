from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'collect.views.index', name='index'),
    url(r'^dashboard/$', 'collect.views.dashboard', name='dashboard'),
    url(r'^account/$', 'collect.views.account', name='my account'),

    url(r'^dashboard/collection/new/', 'collect.views.new_collection', name='new collection'),
    url(r'^dashboard/collection/delete/(?P<collection_id>[0-9]+)/', 'collect.views.delete_collection', name='delete collection'),
    url(r'^dashboard/collection/start/(?P<collection_id>[0-9]+)/', 'collect.views.start_collection', name='start collection'),
    url(r'^dashboard/collection/stop/(?P<collection_id>[0-9]+)/', 'collect.views.stop_collection', name='stop collection'),
    url(r'^dashboard/collection/edit/(?P<collection_id>[0-9]+)/', 'collect.views.edit_collection', name='edit collection'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'redirect_field_name':'next_page'}, name='logout'),
    url('^' + settings.LOGIN_URL[1:] + '$', 'collect.views.collect_login', name='login'),
    url(r'^change-password/$', 'django.contrib.auth.views.password_change', name='password change'),
    url(r'^password-changed/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),
    url(r'^signup/$', 'collect.views.signup', name='signup'),    

)