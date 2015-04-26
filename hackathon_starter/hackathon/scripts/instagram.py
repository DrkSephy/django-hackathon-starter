'''
instagram.py contains a handful of methods for interacting
with Instagram data and returning the responses as JSON.
'''

import requests
import urllib
import urllib2
import json
import simplejson as json2
import googlemaps
from django.conf import settings
from datetime import datetime

AUTHORIZATION_URL = 'https://api.instagram.com/oauth/authorize/?client_id='
ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'

class InstagramOauthClient(object):
    '''
    Python Client for Instagram API.
    '''

    access_token = None
    user_data = None
    is_authorized = False

    def __init__(self, client_id, client_secret):
        '''
        Parameters:
            client_id: String
                - The client_id from registering application
                  on Instagram.
            client_secret: String
                - The client_secret from registering application
                  on Instagram.
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

        redirectUri = '&redirect_uri=http://127.0.0.1:8000/hackathon/&response_type=code'
        authURL = AUTHORIZATION_URL + self.client_id + redirectUri
        #print authURL
        return authURL

    def get_access_token(self, code):
        '''
        Obtains access token.

        Parameters:
            code: String
                - The code is retrieved from the authorization url parameter
                  to obtain access_token.
        '''

        authSetting = {
            'client_id' : self.client_id,
            'client_secret' : self.client_secret,
            'grant_type' : 'authorization_code',
            'redirect_uri' : 'http://127.0.0.1:8000/hackathon/',
            'code' : code}

        authSettingUrl = urllib.urlencode(authSetting)
        req = urllib2.Request(ACCESS_TOKEN_URL, authSettingUrl)
        content = urllib2.urlopen(req)
        jsonlist = json.load(content)
        self.access_token = jsonlist['access_token']
        self.user_data = jsonlist['user']
        self.is_authorized = True







def searchForLocation(address):
    '''
    Parameters:
        address: String
            - The address is a user input.

    Returns:
        location: Dictionary
            - A dictionary returning the latitude, and longitude
              of an address.
    '''

    gmaps = googlemaps.Client(key=settings.GOOGLEMAP_API_KEY)
    #geocoding and address
    geocodeResult = gmaps.geocode(address)

    if geocodeResult:
        location = geocodeResult[0]['geometry']['location']
        return location


def getTaggedMedia(tag, accessToken):
    '''
    Get recent tagged media.

    Parameters:
        tag: String
            - The tag used to search the most recent media that's tagged with it.

    Returns:
        data: Dictionary
            - A dictionary containing recent tagged 120 media
              counts data pertaining to each media.
    '''

    tagUri = 'https://api.instagram.com/v1/tags/'
    taggedMediaUrl = tagUri + tag + '/media/recent?access_token=' + accessToken
    req = requests.get(taggedMediaUrl)
    content = json2.loads(req.content)
    data = content['data']

    while len(data) <= 100:
        nextUrl = content['pagination']['next_url']
        req = requests.get(nextUrl)
        content = json2.loads(req.content)
        for i in content['data']:
            data.append(i)
    #print len(data)
    return data


def getUserInfo(accessToken):
    '''
    Get user information.

    Parameters:
        access_token: String
            - The access_token given after granting permission
              application access to Instagram data.

    Returns:
        data: Dictionary
            - A dictionary containing user information.
    '''

    userInfo = 'https://api.instagram.com/v1/users/32833691/?access_token='+accessToken
    req = requests.get(userInfo)
    content = json2.loads(req.content)
    data = content['data']
    return data


def getUserMedia(userId, accessToken):
    '''
    Parameters:
        accessToken: String
            - The access_token given after granting permission
              application access to Instagram data.
        userId: Integer
            - User's instagram ID number.

    Returns:
        data: Dictionary
            - A dictionary containing user media information.
    '''

    userMediaUri = 'https://api.instagram.com/v1/users/' + str(userId)
    userMedia = userMediaUri + '/media/recent/?access_token=' + accessToken
    req = requests.get(userMedia)
    content = json2.loads(req.content)
    data = content['data']
    return data


def searchLocationIds(lat, lng, accessToken):
    '''
    Parameters:
        lat: Float
            - The latitude of the input address
        lng: Float
            - The longitude of the input address

    Returns:
        listOfIds: Dictionary
            - A dictionary returning the list of location ids
              of the given address coordinates.
    '''

    locIdUri = 'https://api.instagram.com/v1/locations/search?lat=' + str(lat)
    location = locIdUri+'&lng='+str(lng)+'&access_token='+ accessToken+'&distance=5000'
    req = requests.get(location)
    data = json2.loads(req.content)
    listOfIds = []
    if data['meta']['code'] != 200:
        raise Exception("Invalid response %s." % data['meta']['code'])
    searchIds = data['data']
    for data in searchIds:
        for i in data:
            if i == 'id':
                listOfIds.append(data[i])
    return listOfIds


def searchLocationMedia(listOfLocationIds, accessToken):
    '''
    Parameters:
        listOfLocationIds: Float
            - list of location ids retrieve from coordinate of
              of searched address.
        access_token: String
            - The access_token given after granting permission
              application access to Instagram data.

    Returns:
        media: Dictionary
            - A dictionary returning the list of recent media
              of the list of location ids.
    '''

    media = []
    locationUri = 'https://api.instagram.com/v1/locations/'
    for location in listOfLocationIds:
        mediaByLocation = locationUri+location+'/media/recent?access_token='+ accessToken
        req = requests.get(mediaByLocation)
        contentAll = json2.loads(req.content)
        if contentAll['pagination']:
            tempMedia = []
            nextUrl = contentAll['pagination']['next_url']
            req = requests.get(nextUrl)
            content = json2.loads(req.content)
            for i in content['data']:
                i['created_time'] = datetime.fromtimestamp(int(i['created_time']))
                i['created_time'] = i['created_time'].strftime('%Y-%m-%d %H:%M:%S')
                tempMedia.append(i)
            media += [tempMedia]
        else:
            for i in contentAll['data']:
                for data in i:
                    if data == 'created_time':
                        i[data] = datetime.fromtimestamp(int(i[data]))
                        i[data] = i[data].strftime('%Y-%m-%d %H:%M:%S')
            media.append(contentAll['data'])
    return media
