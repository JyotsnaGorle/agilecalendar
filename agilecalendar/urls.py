from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('agcal/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agcal/', include('agcal.urls'))
]
