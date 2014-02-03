__author__ = 'sahith'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('resumeuploader.views',
     url(r'^$', 'login', name='login'),
     url(r'^form$', 'form', name='form'),
)