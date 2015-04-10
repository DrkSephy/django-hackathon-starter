# Django
from django.shortcuts import render
from hackathon.forms import UserForm
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Scripts
from scripts.steam import gamesPulling, steamIDPulling 
from scripts.github import *
from scripts.tumblr import *

# Python
import oauth2 as oauth
import cgi

# Models
from hackathon.models import Profile

getTumblr = TumblrOauthClient(settings.TUMBLR_CONSUMER_KEY, settings.TUMBLR_CONSUMER_SECRET)

consumer = oauth.Consumer(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://twitter.com/oauth/request_token'
access_token_url = 'https://twitter.com/oauth/access_token'
authenticate_url = 'http://twitter.com/oauth/authenticate'

def twitter_login(request):
    # Step 1. Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    # Step 2. Store the request token in a session for later use.
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    # Step 3. Redirect the user to the authentication URL.
    url = "%s?oauth_token=%s" % (authenticate_url,
        request.session['request_token']['oauth_token'])

    return HttpResponseRedirect(url)

@login_required
def twitter_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')

def twitter_authenticated(request):
    # Step 1. Use the request token in the session to build a new client.
    token = oauth.Token(request.session['request_token']['oauth_token'],
        request.session['request_token']['oauth_token_secret'])
    client = oauth.Client(consumer, token)

    # Step 2. Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, "GET")
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response from Twitter.")
    access_token = dict(cgi.parse_qsl(content))

    # Step 3. Lookup the user or create them if they don't exist.
    try:
        user = User.objects.get(username=access_token['screen_name'])
        print user
    except User.DoesNotExist:
        # When creating the user I just use their screen_name@twitter.com
        # for their email and the oauth_token_secret for their password.
        # These two things will likely never be used. Alternatively, you 
        # can prompt them for their email here. Either way, the password 
        # should never be used.
        user = User.objects.create_user(access_token['screen_name'],
            '%s@twitter.com' % access_token['screen_name'],
            access_token['oauth_token_secret'])
        print user

        # Save our permanent token and secret for later.
        profile = Profile()
        profile.user = user
        profile.oauth_token = access_token['oauth_token']
        profile.oauth_secret = access_token['oauth_token_secret']
        profile.save()

    # Authenticate the user and log them in using Django's pre-built 
    # functions for these things.
    user = authenticate(username=access_token['screen_name'],
        password=access_token['oauth_token_secret'])
    login(request, user)

    return HttpResponseRedirect('/')


def index(request):
    context = {'hello': 'world'}
    return render(request, 'hackathon/index.html', context)

def test(request):
    return HttpResponse('meow')

def api_examples(request):
    obtain_oauth_verifier = getTumblr.get_authorize_url()#simpleoauthurl(settings.TUMBLR_CONSUMER_KEY, settings.TUMBLR_CONSUMER_SECRET)
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

