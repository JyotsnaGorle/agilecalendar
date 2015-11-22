from django.conf.urls import patterns, url

from agcal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^api/login/(?P<username>[\w\-]+)/$',
                           views.login, name='login'),
                       url(r'^api/logout/(?P<username>[\w\-]+)/$',
                           views.logout, name='logout'),
                       url(r'^api/user/(?P<username>[\w\-]+)/$', views.user, name='user'),
                       url(r'^api/card/$', views.card, name='card'))
