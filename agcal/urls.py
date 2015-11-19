from django.conf.urls import patterns, url
from agcal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^api/login-user/$',
                           views.login_user, name='login_user'),
                       url(r'^api/logout-user/$',
                           views.logout_user, name='logout_user'),
                       url(r'^api/user/(?P<username>[\w\-]+)/$', views.user, name='user'),
                       url(r'^api/user/$', views.user, name='user'),
                       url(r'^api/card/$', views.card, name='card'))
