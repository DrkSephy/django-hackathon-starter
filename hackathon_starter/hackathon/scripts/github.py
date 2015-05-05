'''
github.py contains a handful of methods for interacting
with Github data and returning the responses as JSON.
'''

import requests
import simplejson as json
import urllib, urlparse

########################
# GITHUB API CONSTANTS #
########################

API_BASE_URL = 'https://api.github.com/users/'

AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

class GithubOauthClient(object):
    '''
    Python Client for Github API.
    '''
    access_token = None
    token_type = None

    def __init__(self, client_id, client_secret):
        '''
        Parameters:
            client_id: String
                - The client_id from registering application
                  on Github.
            client_secret: String
                - The client_secret from registering application
                  on Github.
        '''
        self.client_id = client_id
        self.client_secret = client_secret

    def get_authorize_url(self):
        '''
        Obtains authorize url link with given client_id.

        Returns:
            authURL: String
                - The authorization url.
        '''

        authSetting = {'client_id': self.client_id,
                       'redirect_uri': 'http://127.0.0.1:8000/hackathon/',
                       'scope': 'user, public_repo, repo, repo_deployment, notifications, gist'}
        params = urllib.urlencode(authSetting)
        authURL = AUTHORIZE_URL + '?' + params

        return authURL

    def get_access_token(self, code):
        '''
        Obtains access token.

        Parameters:
            code: String
                - The code is retrieved from the authorization url parameter
                  to obtain access_token.
        '''

        settings = {'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'code': code,
                    'redirect_uri': 'http://127.0.0.1:8000/hackathon/',
                    'accept': 'json'}
        params = urllib.urlencode(settings)
        accessLink = ACCESS_TOKEN_URL + '?' + params
        req = requests.get(accessLink)

        if int(req.status_code) != 200:
            raise Exception('Invalid response %s' %req.status_code)

        content = urlparse.parse_qs(req.content)
        self.access_token = content['access_token'][0]
        self.token_type = content['token_type'][0]
        self.scopes = content['scope'][0]

    def getUserInfo(self):
        '''
        Obtains user information.

        Returns:
            content: Dictionary
                - A dictionary containing user information.
        '''

        link = 'https://api.github.com/user?access_token=' + self.access_token
        req = requests.get(link)

        if int(req.status_code) != 200:
            raise Exception('Invalid response %s' %req.status_code)

        content = json.loads(req.content)
        self.username = content['login']
        return content

def getUserData(user, clientID, clientSecret):
    '''
    Returns data found on a Github User's public profile.
    This includes information such as number of followers,
    e-mail, number of repositories and more.

    Parameters:
        clientID: String
            - The clientID from registering this application
              on Github.
        clientSecret: String
            - The clientSecret from registering this application
            on Github.

    Returns:
        parsedData: Dictionary
            - A dictionary containing the following data:
                - userData['name']
                    - The user's public name on Github
                - userData['blog']
                    - Link to the user's blog on Github
                - userData['email']
                    - The user's public e-mail on Github
                - userData['public_gists']
                    - The number of the user's public gists
                - userData['public_repos']
                    - The number of public repositories owned
                - userData['avatar_url']
                    - Link to user's public avatar
                - userData['followers']
                    - Number of followers
                - userData['following']
                    - Number of users being followed
    '''
    url = API_BASE_URL + user +  '?' + clientID + '&' + clientSecret
    print url
    req = requests.get(url)
    jsonList = []
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)

    return parsedData

def getUserRepositories(user, clientID, clientSecret):
    '''
    Returns a list of all the public repositories
    owned by a User.

    Parameters:
        clientID: String
            - The clientID from registering this application
              on Github.
        clientSecret: String.
            - The clientSecret from registering this application
            on Github.

    Returns:
        repositories: List
            - A list containing all public repository names
              belonging to a user.
    '''
    pageNumber = 1
    jsonList = []
    repositories = []

    while True:
        req = requests.get('https://api.github.com/users/' + user + '/repos?page=' \
            + str(pageNumber) + '&' + clientID + '&' + clientSecret)
        jsonList.append(json.loads(req.content))
        if len(json.loads(req.content)) < 30:
            break
        elif len(json.loads(req.content)) >= 30:
            pageNumber += 1
    for data in jsonList:
        for datum in data:
            repositories.append(datum['name'])
    return repositories

def getForkedRepositories(user, clientID, clientSecret):
    '''
    Returns a list of all the public forked repositories
    owned by a User.

    Parameters:
        clientID: String
            - The clientID from registering this application
              on Github.
        clientSecret: String.
            - The clientSecret from registering this application
            on Github.

    Returns:
        forkedRepositories: List
            - A list containing all forked repository names
              belonging to a user.
    '''

    pageNumber = 1
    jsonList = []
    forkedRepositories = []
    while True:
        req = requests.get('https://api.github.com/users/' + user + '/repos?page=' \
            + str(pageNumber) + '&' + clientID + '&' + clientSecret)
        jsonList.append(json.loads(req.content))
        if len(json.loads(req.content)) < 30:
            break
        elif len(json.loads(req.content)) >= 30:
            pageNumber += 1


    forkedRepos = {}
    for data in jsonList:
        for datum in data:
            if datum['fork'] == True:
                forkedRepos['name'] = datum['name']
                forkedRepositories.append(forkedRepos)
                forkedRepos = {}

    return forkedRepositories

def getTopContributedRepositories(user, repos, clientID, clientSecret):
    '''
    Returns a list containing the commit totals for all
    repositories owned by a user.

    Parameters:
        clientID: String
            - The clientID from registering this application
              on Github.
        clientSecret: String
            - The clientSecret from registering this application
            on Github.

    Returns:
        parsedData: Dictionary
            - A dictionary containing the following data:
                - commits['author']
                    - The name of the committer
                - commits['total']
                    - Total commit count for a user in a repository
                - commits['repo_name']
                    - The name of the repository being tallied
    '''
    jsonList = []
    for repo in repos:
        req = requests.get('https://api.github.com/repos/' + user + '/' + repo \
            + '/stats/contributors' + '?' + clientID + '&' + clientSecret)
        jsonList.append(json.loads(req.content))

    parsedData = []

    indexNumber = -1
    for item in jsonList:
        indexNumber += 1
        commits = {}
        for data in item:
            if data['author']['login'] == user:
                commits['author'] = data['author']['login']
                commits['total'] = data['total']
                commits['repo_name'] = repos[indexNumber]
                parsedData.append(commits)

    return parsedData

def filterCommits(data):
    '''
    Returns the top 10 committed repositories.

    Parameters:
        data: List
            - A list containing commit counts for all
            of a user's public repositories

    Returns:
        maxCommits: List
            - A list containing the top ten repositories
            with the maximum number of commits by a user
    '''

    maxCommits = []
    i = 0
    while i < 10:
        maxCommitedRepo = max(data, key=lambda x: x['total'])
        maxCommits.append(maxCommitedRepo)
        index = data.index(maxCommitedRepo)
        data.pop(index)
        i += 1
    return maxCommits

def getStarGazerCount(user, clientID, clientSecret):
    '''
    Returns a list number of stargazers for each
    of a user's public repositories.

    Parameters:
        clientID: String
            - The clientID from registering this application
              on Github.
        clientSecret: String
            - The clientSecret from registering this application
            on Github.

    Returns:
        stargazers: Dictionary
            - A dictionary containing the following data:
                - starData['stargazers_count']
                    - The number of stargazers for a given repository
                - starData['name']
                    - The name of the repository being observed
    '''
    pageNumber = 1
    jsonList = []
    stargazers = []
    while True:
        req = requests.get('https://api.github.com/users/' + user + '/repos?page=' \
            + str(pageNumber) + '&' + clientID + '&' + clientSecret)
        jsonList.append(json.loads(req.content))
        if len(json.loads(req.content)) < 30:
            break
        elif len(json.loads(req.content)) >= 30:
            pageNumber += 1


    for data in jsonList:
        for datum in data:
            starData = {}
            starData['stargazers_count'] = datum['stargazers_count']
            starData['name'] = datum['name']
            stargazers.append(starData)

    return stargazers

def filterStarGazerCount(data):
    '''
    Returns the top 10 stargazed repositories.

    Parameters:
        data: List
            - A list containing stargazer counts for all
            of a user's public repositories

    Returns:
        maxStars: List
            - A list containing the top ten repositories
            with the maximum number of stargazers
    '''
    maxStars = []
    i = 0
    while i < 10:
        maxStarGazers = max(data, key=lambda x: x['stargazers_count'])
        maxStars.append(maxStarGazers)
        index = data.index(maxStarGazers)
        data.pop(index)
        i += 1
    return maxStars




