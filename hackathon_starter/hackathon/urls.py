from django.conf.urls import patterns, url

from hackathon import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api/$', views.api_examples, name='api'),
    url(r'^steam/$', views.steam, name='steam'),
    url(r'^githubResume/$', views.githubResume, name='githubResume'),
    url(r'^githubUser/$', views.githubUser, name='githubUser'),
    url(r'^githubTopRepositories/$', views.githubTopRepositories, name='githubTopRepositories'),
    url(r'^tumblr/$', views.tumblr, name='tumblr'),
    url(r'^linkedin/$', views.linkedin, name='linkedin'),
    url(r'^snippets/$', views.snippet_list, name='snippets'),
    url(r'^twilio/$', views.twilio, name='twilio'),
)
