from django.conf.urls import patterns, url
import views


urlpatterns = patterns(
    'blongo.views.',
    url(r'^$', views.index, name='index'),
)
