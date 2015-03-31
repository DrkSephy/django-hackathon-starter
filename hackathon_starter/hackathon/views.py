from django.shortcuts import render
from hackathon.forms import UserForm
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from scripts.steam import gamesPulling, steamIDPulling 
from scripts.github import getUserData, getUserRepositories, getTopContributedRepositories, filterCommits
from scripts.tumblr import getUserInfo as tumblrUserInfo
from scripts.tumblr import getBlogInfo as tumblrBlogInfo


def index(request):
	context = {'hello': 'world'}
	return render(request, 'hackathon/index.html', context)

def test(request):
	return HttpResponse('meow')

def api_examples(request):
    context = {'title': 'API Examples Page'}
    return render(request, 'hackathon/api_examples.html', context)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'hackathon/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/hackathon/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Django Hackathon account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'hackathon/login.html', {})

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/hackathon/')

def steam(request):
    #Should link to test of Steam API example.
    key = '231E98D442E52B87110816C3D5114A1D'
    SteamUN = "Marorin"
    steamID = steamIDPulling(SteamUN, key)
    game = gamesPulling(steamID, key)
    return render(request,'hackathon/steam.html', {"game": game })

def github(request):
    userData = getUserData()
    #Get a list of all the user's repositories
    repositories = getUserRepositories()
    #Get a list of all commit statistics for all repositories
    list = getTopContributedRepositories(repositories)
    # Get a list of the top 10 most committed repositories
    filtered = filterCommits(list)
    # Store data into a dictionary for rendering
    allData['userData'] = userData
    allData['filteredData'] = filtered
    
    return render(request, 'hackathon/github.html', { 'data': userData })

def tumblr(request):
    meta, response, blog = tumblrBlogInfo('david')
    context = {'title': 'Tumblr Example', 'blogData': blog}
    return render(request, 'hackathon/tumblr.html', context)

def linkedin(request):
    context = {'title': 'linkedin Example'}
    return render(request, 'hackathon/linkedin.html', context)

