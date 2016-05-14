"""
Definition of urls for Face_Recognition_API.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^face_detection/detect/$', 'face_detector.views.detect'),
    url(r'^face_recognition/api/$', 'face_recognition.views.recognition'),
    # Examples:
    url(r'^$', 'Face_Recognition_API.views.home', name='home'),
    # url(r'^Face_Recognition_API/', include('Face_Recognition_API.Face_Recognition_API.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
