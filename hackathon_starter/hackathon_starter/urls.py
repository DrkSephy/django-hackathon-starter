from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^hackathon/', include('hackathon.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^openid/(.*)', SessionConsumer()),
)
