from django.shortcuts import render
from hackathon.forms import UserForm
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from scripts.steam import gamesPulling, steamIDPulling 
from scripts.github import *
from scripts.tumblr import *
from django.conf import settings



def index(request):
    context = {'hello': 'world'}
    return render(request, 'hackathon/index.html', context)

def test(request):
    return HttpResponse('meow')

def api_examples(request):
    context = {'title': 'API Examples Page'}
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
    #get blogger twitterthecomic's blog information
    blog = getBlogInfo('twitterthecomic', settings.TUMBLR_CONSUMER_KEY)
    #get tags that was tagged along starbucks
    tagged_blog = getTaggedInfo("starbucks", settings.TUMBLR_CONSUMER_KEY)
    #get blog information tagged with starbucks
    blogontag = getTaggedBlog("starbucks", settings.TUMBLR_CONSUMER_KEY)
    context = {'title': "What's up Starbucks?", 'blogData': blog, 'blogTag': tagged_blog, 'blogontag': blogontag}
    return render(request, 'hackathon/tumblr.html', context)

def linkedin(request):
    userinfo = getUserInfo()
    context = {'title': 'linkedin Example','userdata': userinfo}
    return render(request, 'hackathon/linkedin.html', context)

