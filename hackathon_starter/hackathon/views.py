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
from scripts.steam import gamespulling, steamidpulling 
from scripts.github import *
from scripts.tumblr import TumblrOauthClient
from scripts.twilioapi import *
from scripts.instagram import InstagramOauthClient
from scripts.scraper import steamDiscounts
from scripts.quandl import *

# Python
import oauth2 as oauth
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Models
from hackathon.models import Snippet, Profile
from hackathon.serializers import SnippetSerializer
from hackathon.forms import UserForm


getTumblr = TumblrOauthClient(settings.TUMBLR_CONSUMER_KEY, settings.TUMBLR_CONSUMER_SECRET)
getInstagram = InstagramOauthClient(settings.INSTAGRAM_CLIENT_ID, settings.INSTAGRAM_CLIENT_SECRET)

def index(request):
    context = {'hello': 'world'}
    return render(request, 'hackathon/index.html', context)


##################
#  API Examples  #
##################

def api_examples(request):
    instagram_url =getInstagram.get_authorize_url()
    if not getTumblr.accessed:
        obtain_oauth_verifier = getTumblr.authorize_url()
    else:
        obtain_oauth_verifier = '/hackathon/tumblr'
    #obtain_oauth_verifier = getTumblr.authorize_url()
    context = {'title': 'API Examples Page', 'tumblr_url': obtain_oauth_verifier, 'instagram_url':instagram_url}
    return render(request, 'hackathon/api_examples.html', context)

#################
#   STEAM API   #
#################

def steam(request):
    #Should link to test of Steam API example.
    key = '231E98D442E52B87110816C3D5114A1D'
    SteamUN = "Marorin"
    steamID = steamidpulling(SteamUN, key)
    game = gamespulling(steamID, key)
    return render(request,'hackathon/steam.html', {"game": game })

def steamDiscountedGames(request):
    data = steamDiscounts()
    return JsonResponse({ 'data': data })

#################
#  FACEBOOK API #
#################

def facebook(request):
    '''A sample application that will publish a status update after going into the login process using the Javascript SDK '''
    yourappid = '364831617044713'
    return render(request, 'hackathon/facebook.html', { 'yourappid' : yourappid })

#################
#   QUANDL API  #
#################

def quandlDowJones(request):
    '''Returns JSON response about the latest dowjones index.'''
    APIKEY = ' fANs6ykrCdAxas7zpMz7'
    parsedData = dowjonesIndustrialAvg(APIKEY)
    return JsonResponse({'data': parsedData})

def quandlSnp500(request):
    '''Returns JSON response about the latest SNP 500 index.'''
    APIKEY = ' fANs6ykrCdAxas7zpMz7'
    parsedData = snp500IndexPull(APIKEY)
    return JsonResponse({'data': parsedData})

def quandlNasdaq(request):
    '''Returns JSON response about the latest nasdaq index.'''
    APIKEY = ' fANs6ykrCdAxas7zpMz7'
    parsedData = nasdaqPull(APIKEY)
    return JsonResponse({'data': parsedData})

#################
#   GITHUB API  #
#################


def githubUser(request):
    '''Returns JSON response about a specific Github User'''

    parsedData = {}
    parsedData['userData'] = getUserData(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    return JsonResponse({ 'data': parsedData })

def githubTopRepositories(request):
    '''Returns JSON response of a User's Top Committed repositories'''

    parsedData = {}
    repositories = getUserRepositories(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    list = getTopContributedRepositories(repositories, settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET)
    filtered = filterCommits(list)
    parsedData['committed'] = filtered
    return JsonResponse({ 'data': parsedData })

def githubResume(request):
    '''A sample application which pulls various Github data to form a Resume of sorts'''
    
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


#################
#   TUMBLR API  #
#################

def tumblr(request):
    ''' Tumblr api calls '''
    if not getTumblr.accessed:
        oauth_verifier = request.GET.get('oauth_verifier')
        getTumblr.access_token_url(oauth_verifier)
    if request.user not in User.objects.all():
        try:
            user_info, total_blog = getTumblr.getUserInfo()
            username = str(user_info['name'])+ "2"
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user_info, total_blog = getTumblr.getUserInfo()
            username = str(user_info['name'])+ "2"
            new_user = User.objects.create_user(username, username+'@example.com','password')
            new_user.save()
            profile =Profile()
            profile.user = new_user
            profile.oauth_token = getTumblr.oauth_token
            profile.oauth_secret = getTumblr.oauth_token_secret
            profile.save()

        user = authenticate(username=username, password='password')
        login(request, user)

    #get blogger twitterthecomic's blog information
    blog = getTumblr.getBlogInfo('twitterthecomic')
    #get tags that was tagged along starbucks
    tagged_blog = getTumblr.getTaggedInfo("starbucks")
    #get blog information tagged with starbucks
    blogontag = getTumblr.getTaggedBlog("starbucks")

    context = {'title': "What's up Starbucks?", 'blogData': blog, 'blogTag': tagged_blog, 'blogontag': blogontag}
    return render(request, 'hackathon/tumblr.html', context)


####################
#   INSTAGRAM API  #
####################

def instagram(request):
    code = request.GET['code']
    getInstagram.get_access_token(code)

    if request.user not in User.objects.all():
        try:  
            user = User.objects.get(username=getInstagram.user_data['username'] )
        except User.DoesNotExist:
            username = getInstagram.user_data['username']
            new_user = User.objects.create_user(username, username+'@example.com', 'password')
            new_user.save()
            profile = Profile()
            profile.user = new_user
            profile.oauth_token = getInstagram.client_id
            #since instagram doesnt have oauth_secret value, using this field to temp set in access token
            # for JSON response
            profile.oauth_secret = getInstagram.access_token 
            profile.save()

        user = authenticate(username=getInstagram.user_data['username'], password='password')
        login(request, user)

    search_tag = 'kitten'
    #return tagged objects
    tagged_media = getInstagram.get_tagged_media(search_tag)
    context = {'title': 'Instagram', 'tagged_media': tagged_media, 'search_tag': search_tag}
    return render(request, 'hackathon/instagram.html', context)

def instagramUser(request):
    ''' Returns JSON response about a specific Instagram User. '''

    user_id = User.objects.get(username='mk200789').id
    access_token = Profile.objects.get(user=user_id).oauth_secret
    parsedData = getInstagram.get_user_info(access_token)
    return JsonResponse({ 'data': parsedData })

def instagramUserMedia(request):
    ''' Returns JSON response about a specific Instagram User's Media. '''
    user_id = User.objects.get(username='mk200789').id
    access_token = Profile.objects.get(user=user_id).oauth_secret
    parsedData = getInstagram.get_user_media(32833691,access_token)
    return JsonResponse({'data': parsedData })

def instagramMediaByLocation(request):
    if request.method == 'GET':
        if request.GET.items():
            if request.user in User.objects.all():
                address = request.GET.get('address_field')
                user_id = User.objects.get(username=request.user).id
                access_token = Profile.objects.get(user=user_id).oauth_secret
                #lat, lng = getInstagram.search_for_location(address, access_token)
                geocode_result = getInstagram.search_for_location(address, access_token)
                if geocode_result:
                    location_ids =getInstagram.search_location_ids(geocode_result['lat'], geocode_result['lng'], access_token)
                    media = getInstagram.search_location_media(location_ids, access_token)
                    title = address
        else:
            title, media,location_ids, geocode_result = 'Media by location', '','', ''


    context = {'title': title, 'geocode_result':geocode_result, 'media':media, 'list_id':location_ids}
    return render(request, 'hackathon/instagram_q.html', context)


##################
#  LINKED IN API #
##################

def linkedin(request):
    userinfo = getUserInfo()
    context = {'title': 'linkedin Example','userdata': userinfo}
    return render(request, 'hackathon/linkedin.html', context)


#########################
# Snippet RESTful Model #
#########################

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


##################
#   Twilio API   #
##################

def twilio(request):
    # Test credentials
    # sendSMS('Meow', '+13473282978', '+13473781813')
    if request.method == 'POST':
        number = request.POST.get('number')
        message = request.POST.get('message')
        sendSMS(str(message), str(number), '+13473781813')
        context = {'message': 'Your message has been sent successfully!'}
        return HttpResponseRedirect('/hackathon/api/')
    return render(request, 'hackathon/twilio.html')


######################
# Registration Views #
######################

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


def instagram_login(request):
    instagram_url =getInstagram.get_authorize_url()
    return HttpResponseRedirect(instagram_url)

def tumblr_login(request):
    tumblr_url = getTumblr.authorize_url()
    return HttpResponseRedirect(tumblr_url)
