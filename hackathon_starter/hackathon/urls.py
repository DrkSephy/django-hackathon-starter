from django.conf.urls import patterns, url

from hackathon import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api/$', views.api_examples, name='api'),
    url(r'^steam/$', views.steam, name='steam')
)
