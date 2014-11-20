from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns(
    'app.views',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^better/$', views.better, name='better'),
)
