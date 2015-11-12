from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agcal/', include('agcal.urls'))
]
