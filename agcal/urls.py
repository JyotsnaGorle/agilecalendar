from django.conf.urls import patterns, url

from agcal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^api/login/(?P<username>[\w\-]+)/$', views.login),
                       url(r'^api/login/(?P<username>[\w\-]+)$', views.login),
                       url(r'^api/logout/(?P<username>[\w\-]+)/$', views.logout),
                       url(r'^api/logout/(?P<username>[\w\-]+)$', views.logout),
                       url(r'^api/user/(?P<username>[\w\-]+)/$', views.user),
                       url(r'^api/user/(?P<username>[\w\-]+)$', views.user),
                       url(r'^api/user/(?P<username>[\w\-]+)/boards$', views.boards),
                       url(r'^api/user/(?P<username>[\w\-]+)/boards/$', views.boards),
                       url(r'^api/user/(?P<username>[\w\-]+)/board/(?P<board_id>[\w\-]+)$', views.board),
                       url(r'^api/user/(?P<username>[\w\-]+)/board/(?P<board_id>[\w\-]+)/$', views.board))
