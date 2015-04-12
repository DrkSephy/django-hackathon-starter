# Django
from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Scripts
from scripts.steam import gamesPulling, steamIDPulling 
from scripts.github import *
from scripts.tumblr import *
from scripts.twilioapi import *

# Python
import oauth2 as oauth
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Models
from hackathon.models import Snippet
from hackathon.serializers import SnippetSerializer
from hackathon.forms import UserForm


getTumblr = TumblrOauthClient(settings.TUMBLR_CONSUMER_KEY, settings.TUMBLR_CONSUMER_SECRET)

def index(request):
    context = {'hello': 'world'}
    return render(request, 'hackathon/index.html', context)

def twilio(request):
    sendSMS('Meow', '+13473282978', '+13473781813')
    return render(request, 'hackathon/twilio.html')

def api_examples(request):
    obtain_oauth_verifier = getTumblr.get_authorize_url()
    #simpleoauthurl(settings.TUMBLR_CONSUMER_KEY, settings.TUMBLR_CONSUMER_SECRET)
    context = {'title': 'API Examples Page', 'tumblr_url': obtain_oauth_verifier}
    return render(request, 'hackathon/api_examples.html', context)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    
    return render(request,
            'hackathon/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hackathon/')
            else:
                return HttpResponse("Your Django Hackathon account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'hackathon/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/hackathon/')

def steam(request):
    #Should link to test of Steam API example.
    key = '231E98D442E52B87110816C3D5114A1D'
    SteamUN = "Marorin"
    steamID = steamIDPulling(SteamUN, key)
    game = gamesPulling(steamID, key)
    return render(request,'hackathon/steam.html', {"game": game })

def github(request):
    allData = {}
    userData = getUserData(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    repositories = getUserRepositories(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    list = getTopContributedRepositories(repositories, settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    filtered = filterCommits(list)
    stargazers = getStarGazerCount(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    filteredStargazers = filterStarGazerCount(stargazers)
    forkedRepos = getForkedRepositories(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    allData['userData'] = userData
    allData['filteredData'] = filtered
    allData['filteredStargazers'] = filteredStargazers
    allData['forkedRepos'] = forkedRepos
    # return JsonResponse({'data': allData});
    return render(request, 'hackathon/github.html', { 'data': allData })

def tumblr(request):
    ''' Tumblr api calls '''
    #retrieve verifier via url link
    if not request.GET.items():
        return HttpResponseRedirect('/hackathon/api/')
    else:
        getTumblr.get_access_token_url(request.GET.get('oauth_verifier'))
        #get blogger twitterthecomic's blog information
        blog = getTumblr.getBlogInfo('twitterthecomic')
        #get tags that was tagged along starbucks
        tagged_blog = getTumblr.getTaggedInfo("starbucks")
        #get blog information tagged with starbucks
        blogontag = getTumblr.getTaggedBlog("starbucks")
        context = {'title': "What's up Starbucks?", 'blogData': blog, 'blogTag': tagged_blog, 'blogontag': blogontag}
        return render(request, 'hackathon/tumblr.html', context)

def linkedin(request):
    userinfo = getUserInfo()
    context = {'title': 'linkedin Example','userdata': userinfo}
    return render(request, 'hackathon/linkedin.html', context)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

