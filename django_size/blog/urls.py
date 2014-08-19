from django.conf.urls import patterns, include, url
from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^index$', views.index),
    url(r'^home$', views.article_list),
    url(r'^login$', views.login_view),
)