from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', include('app.urls')),
    url(r'^', include('app.urls')),
    url(r'^about/', include('app.urls'))
)
