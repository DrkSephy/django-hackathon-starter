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
from scripts.instagram import *
from scripts.scraper import steamDiscounts
from scripts.quandl import *
from scripts.twitter import TwitterOauthClient
from scripts.nytimes import *

# Python
import oauth2 as oauth
import simplejson as json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Models
from hackathon.models import Snippet, Profile, InstagramProfile, TwitterProfile, MeetupToken
from hackathon.serializers import SnippetSerializer
from hackathon.forms import UserForm


getTumblr = TumblrOauthClient(settings.TUMBLR_CONSUMER_KEY, settings.TUMBLR_CONSUMER_SECRET)
getInstagram = InstagramOauthClient(settings.INSTAGRAM_CLIENT_ID, settings.INSTAGRAM_CLIENT_SECRET)
getTwitter = TwitterOauthClient(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

def index(request):
    print "index: " + str(request.user)

    if not request.user.is_active:
        if request.GET.items():
            if 'oauth_verifier' in request.GET.keys():
                oauth_verifier = request.GET['oauth_verifier']
                getTwitter.get_access_token_url(oauth_verifier) 

                try:
                    user = User.objects.get(username = getTwitter.username + '_twitter')#(username=getTwitter.username)
                except User.DoesNotExist:
                    username = getTwitter.username + '_twitter'
                    new_user = User.objects.create_user(username, username+'@madewithtwitter.com', 'password')
                    new_user.save()
                    profile = TwitterProfile(user = new_user,oauth_token = getTwitter.oauth_token, oauth_token_secret= getTwitter.oauth_token_secret, twitter_user=getTwitter.username)
                    profile.save()
                user = authenticate(username=getTwitter.username+'_twitter', password='password')
                login(request, user)
            elif 'code' in request.GET.keys():
                code = request.GET['code']
                getInstagram.get_access_token(code)

                try: 
                    user = User.objects.get(username=getInstagram.user_data['username']+'_instagram')
                except User.DoesNotExist:
                    username = getInstagram.user_data['username']+'_instagram'
                    new_user = User.objects.create_user(username, username+'@madewithinstagram.com', 'password')
                    new_user.save()
                    profile = InstagramProfile(user = new_user, access_token = getInstagram.access_token, instagram_user=getInstagram.user_data['username'])
                    profile.save()
                user = authenticate(username=getInstagram.user_data['username']+'_instagram' , password='password')
                login(request, user)
    else:
        if request.GET.items():
            if 'oauth_verifier' in request.GET.keys():
                oauth_verifier = request.GET['oauth_verifier']
                getTwitter.get_access_token_url(oauth_verifier)
                user = User.objects.get(username = request.user.username)

                try:
                    twitterUser = TwitterProfile.objects.get(user = user.id)
                except TwitterProfile.DoesNotExist:
                    profile = TwitterProfile(user = user, oauth_token = getTwitter.oauth_token, oauth_token_secret= getTwitter.oauth_token_secret, twitter_user=getTwitter.username)
                    profile.save()
            elif 'code' in request.GET.keys():
                code = request.GET['code']
                getInstagram.get_access_token(code)
                user = User.objects.get(username = request.user.username)

                try: 
                    instagramUser = InstagramProfile.objects.get(user= user.id)
                except InstagramProfile.DoesNotExist:
                    profile = InstagramProfile(user = user, access_token = getInstagram.access_token, instagram_user=getInstagram.user_data['username'])
                    profile.save()

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
#   MEETUP API  #
#################

def meetup(request):
    CONSUMER_KEY = 'p50vftdqq72tgotpaeqk5660un'
    REDIRECT_URI = 'http://127.0.0.1:8000/hackathon/meetupToken'
    AUTHORIZE_URL = 'https://secure.meetup.com/oauth2/authorize?client_id=' + CONSUMER_KEY + '&response_type=code' + '&redirect_uri=' + REDIRECT_URI
    return HttpResponseRedirect(AUTHORIZE_URL)

def meetupToken(request):
    access_token_url = 'https://secure.meetup.com/oauth2/access?'
    CLIENT_KEY = 'p50vftdqq72tgotpaeqk5660un'
    CLIENT_SECRET = 'i5l00ln2r4mcf161n6451hjoj8'
    REDIRECT_URI = 'http://127.0.0.1:8000/hackathon/meetupToken'
    url = access_token_url + 'client_id=' +  CLIENT_KEY + '&client_secret=' + CLIENT_SECRET + '&grant_type=authorization_code' + '&redirect_uri=' + REDIRECT_URI + '&code=' +  request.GET.get('code')

    response = requests.post(url)
    access_token = json.loads(response.content)['access_token']
    # profile = InstagramProfile(user = new_user, access_token = getInstagram.access_token, instagram_user=getInstagram.user_data['username'])
    meetupToken = MeetupToken(access_token = access_token)
    meetupToken.save()
    thing = MeetupToken.objects.all()
    print thing[0]
    req = requests.get("https://api.meetup.com/2/member/self/?access_token=" + access_token)
    print req.content
    return HttpResponseRedirect('http://127.0.0.1:8000/hackathon/api/')


#################
#   QUANDL API  #
#################

def quandlDowJones(request):
    '''Returns JSON response about the latest dowjones index.'''
    APIKEY = 'fANs6ykrCdAxas7zpMz7'
    dowjonesdata = fetchData(APIKEY, 'https://www.quandl.com/api/v1/datasets/BCB/UDJIAD1.json?')
    print dowjonesdata
    return JsonResponse({'data': dowjonesdata})

def quandlSnp500(request):
    '''Returns JSON response about the latest SNP 500 index.'''
    APIKEY = 'fANs6ykrCdAxas7zpMz7'
    snpdata = fetchData(APIKEY, 'https://www.quandl.com/api/v1/datasets/YAHOO/INDEX_GSPC.json?')
    return JsonResponse({'data': snpdata})

def quandlNasdaq(request):
    '''Returns JSON response about the latest nasdaq index.'''
    APIKEY = 'fANs6ykrCdAxas7zpMz7'
    nasdaqdata = fetchData(APIKEY, 'https://www.quandl.com/api/v1/datasets/NASDAQOMX/COMP.json?')
    return JsonResponse({'data': nasdaqdata})

def quandlstocks(request):
    APIKEY = 'fANs6ykrCdAxas7zpMz7'	
    everyData = {}
    dowjonesdata = fetchData(APIKEY, 'https://www.quandl.com/api/v1/datasets/BCB/UDJIAD1.json?')
    everyData['dow'] = dowjonesdata
    snpdata = fetchData(APIKEY, 'https://www.quandl.com/api/v1/datasets/YAHOO/INDEX_GSPC.json?')
    everyData['snp'] = snpdata
    nasdaqdata = fetchData(APIKEY, 'https://www.quandl.com/api/v1/datasets/NASDAQOMX/COMP.json?')
    everyData['nasdaq'] = nasdaqdata
    return render(request, 'hackathon/quandl.html', { 'everyData': everyData })

#################
#  NYTIMES API  #
#################

def nytimespop(request):
    '''Returns JSON response about the most viewed articles for the last 24 hours.'''
    POPAPIKEY = 'be4cd251d8a4f1a3362689088bdb0255:0:71947444'
    popdata = fetcharticle(POPAPIKEY, 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/1.json?')
    return JSONResponse({'data': popdata})

def nytimestop(request):
    '''Returns JSON response about the articles located in the homepage'''
    TOPAPIKEY = 'c9655598e1fd4ff591f6d46f2321260e:17:71947444'
    topdata = fetcharticle(TOPAPIKEY, 'http://api.nytimes.com/svc/topstories/v1/home.json?')
    return JSONResponse({'data': topdata})

def nytimesarticles(request):
    POPAPIKEY = 'be4cd251d8a4f1a3362689088bdb0255:0:71947444'
    TOPAPIKEY = 'c9655598e1fd4ff591f6d46f2321260e:17:71947444'
    everyData = {}
    popdata = fetcharticle(POPAPIKEY, 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/1.json?')
    topdata = topdata = fetcharticle(TOPAPIKEY, 'http://api.nytimes.com/svc/topstories/v1/home.json?')
    everyData['top'] = topdata
    everyData['pop'] = popdata
    return render(request, 'hackathon/nytimes.html', { 'everyData': everyData })

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
            new_user = User.objects.create_user(username, username+'@tumblr.com','password')
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
    #print getInstagram.is_authorized

    if getInstagram.is_authorized:
        search_tag = 'kitten'
        #return tagged objects
        instagramUser = InstagramProfile.objects.get(user=request.user)
        tagged_media = getTaggedMedia(search_tag, instagramUser.access_token)        
    else:
        instagram_url =getInstagram.get_authorize_url()
        return HttpResponseRedirect(instagram_url)
    
    context = {'title': 'Instagram', 'tagged_media': tagged_media, 'search_tag': search_tag}
    return render(request, 'hackathon/instagram.html', context)

def instagramUser(request):
    ''' Returns JSON response about a specific Instagram User. '''

    access_token = InstagramProfile.objects.get(instagram_user='mk200789').access_token
    parsedData = getUserInfo(access_token)
    return JsonResponse({ 'data': parsedData })

def instagramUserMedia(request):
    ''' Returns JSON response about a specific Instagram User's Media. '''

    access_token = InstagramProfile.objects.get(instagram_user='mk200789').access_token
    parsedData = getUserMedia(32833691, access_token)
    return JsonResponse({'data': parsedData })

def instagramMediaByLocation(request):
    print request.user
    if request.method == 'GET':
        if request.GET.items():
            #check if user has a User profile
            if request.user in User.objects.all():
                #check if user has an Instagram profile
                user = User.objects.get(username=request.user)
                #if user has an Instagram profile, query the search
                if InstagramProfile.objects.all().filter(user=user.id):
                    address = request.GET.get('address_field')
                    access_token = InstagramProfile.objects.get(user=user.id).access_token
                    geocode_result = searchForLocation(address)
                    if geocode_result:
                        location_ids = searchLocationIds(geocode_result['lat'], geocode_result['lng'], access_token)
                        media = searchLocationMedia(location_ids, access_token)
                        title = address
                        err_msg = ''
                else:
                    title, media, err_msg, location_ids, geocode_result = 'Media by location','', str(request.user)+ ' does not have an InstagramProfile','', ''
        else:
            title, media, err_msg, location_ids, geocode_result = 'Media by location', '','', '', ''


    context = {'title': title, 'geocode_result':geocode_result, 'media':media, 'list_id':location_ids, 'err_msg': err_msg}
    return render(request, 'hackathon/instagram_q.html', context)


####################
#   TWITTER API    #
####################

def twitter(request):
    if getTwitter.is_authorized:
        value = getTwitter.get_trends_available(settings.YAHOO_CONSUMER_KEY)
    else:
        tumblr_url = getTwitter.get_authorize_url()
        return HttpResponseRedirect(tumblr_url)

    context ={'title': 'twitter', 'value': value}
    return render(request, 'hackathon/twitter.html', context)


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
    instagram_url = getInstagram.get_authorize_url()
    return HttpResponseRedirect(instagram_url)

def tumblr_login(request):
    tumblr_url = getTumblr.authorize_url()
    return HttpResponseRedirect(tumblr_url)

def twitter_login(request):
    twitter_url = getTwitter.get_authorize_url()     
    return HttpResponseRedirect(twitter_url)