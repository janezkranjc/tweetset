from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'collect.views.index', name='index'),
    url(r'^dashboard/$', 'collect.views.dashboard', name='dashboard'),
    url(r'^account/$', 'collect.views.account', name='my account'),

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