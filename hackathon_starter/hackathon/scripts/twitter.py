# pylint: disable=too-many-instance-attributes
# pylint: disable=unused-variable
# pylint: disable=too-many-arguments

'''
twitter.py contains a handful of methods for interacting
with Twitter data and returning the responses as JSON.
'''


import urlparse
import oauth2 as oauth
import requests
import base64, random
import urllib
import binascii
import time, collections, hmac, hashlib
import simplejson as json2
import codecs
import json

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZE_URL = 'https://api.twitter.com/oauth/authorize'

class TwitterOauthClient(object):
    '''
    Python Client for Twitter API.
    '''

    oauth_token = None
    oauth_token_secret = None
    username = None
    is_authorized = False


    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        '''
        Parameters:
            consumer_key: String
                - The consumer_key from registering application
                  on Instagram.
            consumer_secret: String
                - The consumer_secret from registering application
                  on Instagram.
        '''

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.consumer = oauth.Consumer(key=self.consumer_key, secret=self.consumer_secret)


    def get_authorize_url(self):
        '''
        Obtained oauth_token and oauth_token_secret from request_token_url,
        returns an authorize url.

        From the redirect url, we obtain the oauth verifier.

        Returns:
            authURL: String
                - The authorization url.
        '''

        client = oauth.Client(self.consumer)
        resp, content = client.request(REQUEST_TOKEN_URL, 'GET')

        #if int(resp['status']) != 200:
        #    raise Exception('Invalid response %s' %resp['status'])

        requestToken = dict(urlparse.parse_qsl(content))

        #temporary
        self.oauth_token = requestToken['oauth_token']
        self.oauth_token_secret = requestToken['oauth_token_secret']
        #print self.oauth_token

        #link to authorize app access twitter data and return to twitter api example page
        redirectUri = '&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/twitter/'
        authURL = AUTHORIZE_URL+"?oauth_token="+self.oauth_token+redirectUri
        return authURL


    def get_access_token_url(self, oauthVerifier):
        '''
        Get access token from redirect url.

        Parameters:
            oauthVerifier: String
                - A paramater retrieved from scraping the redirect url.

        Returns:
            data: Dictionary
                - A dictionary containing recent tagged 120 media
                  counts data pertaining to each media.
        '''

        token = oauth.Token(self.oauth_token, self.oauth_token_secret)
        token.set_verifier(oauthVerifier)

        client = oauth.Client(self.consumer, token)
        resp, content = client.request(ACCESS_TOKEN_URL, 'POST')

        if int(resp['status']) != 200:
            raise Exception('Invalid response %s' %resp['status'])

        #print content
        accessToken = dict(urlparse.parse_qsl(content))

        #permanent
        self.oauth_token = accessToken['oauth_token']
        self.oauth_token_secret = accessToken['oauth_token_secret']
        self.username = accessToken['screen_name']
        self.is_authorized = True


    def get_tweets(self, tweet):
        '''
        Get tweets of relevant search query.
        '''
        method = 'get'
        link = 'https://api.twitter.com/1.1/search/tweets.json'
        linkParameters = {'q': tweet, 'count': '100', 'result_type': 'popular'}

        oauthParameters = getOauthParameters(
            self.consumer_key,
            self.access_token
        )

        oauthParameters['oauth_signature'] = generateSignature(
            method,
            link,
            linkParameters,
            oauthParameters,
            self.consumer_secret,
            self.access_token_secret
        )

        headers = {'Authorization': createAuthHeader(oauthParameters)}

        link += '?' + urllib.urlencode(linkParameters)

        req = requests.get(link, headers=headers)

        if int(req.status_code) != 200:
            raise Exception('Invalid response %s' %req.status_code)

        content = json2.loads(req.content)

        jsonlist = {}
        for contrib in content['statuses']:
            for e in contrib:
                if e == 'retweet_count':
                    if contrib['user']['screen_name'] in jsonlist:
                        jsonlist[contrib['user']['screen_name']][contrib[e]] = str(contrib['text'].encode('ascii', 'ignore'))
                    else:
                        jsonlist[contrib['user']['screen_name']] = { contrib[e]:str(contrib['text'].encode('ascii', 'ignore'))}
                    

        return content['statuses'], json.dumps(jsonlist)


    def get_trends_available(self, yahooConsumerKey):
        '''
        Get the locations that Twitter has trending topic information for.

        '''

        method = 'get'
        link = 'https://api.twitter.com/1.1/trends/available.json'
        linkParameters = {}

        oauthParameters = getOauthParameters(
            self.consumer_key,
            self.access_token
        )

        oauthParameters['oauth_signature'] = generateSignature(
            method,
            link,
            linkParameters,
            oauthParameters,
            self.consumer_secret,
            self.access_token_secret
        )

        headers = {'Authorization': createAuthHeader(oauthParameters)}

        if linkParameters:
            link += '?'+urllib.urlencode(linkParameters)

        req = requests.get(link, headers=headers)
        #print req.status_code

        if int(req.status_code) != 200:
            raise Exception('Invalid response %s' %req.status_code)

        content = json2.loads(req.content)
        #print len(content)

        for place in content:
            for item in place:
                if item == 'url':
                    url = place[item]+'/neighbors?appid='+yahooConsumerKey+'&format=json'
                    requestNeighborData = requests.get(url)
                    #print request_neighbor_data.status_code
                    if requestNeighborData.status_code == 200:
                        neighbor = json2.loads(requestNeighborData.content)
                    else:
                        neighbor = {}

            place['neighbor'] = neighbor
                    #print place


        return content



def percentEncode(string):
    '''
    Percent encode strings.
    '''
    return urllib.quote(string, safe='~')


def getNonce():
    '''
    Generate unique token per request.
    '''

    nonce = base64.b64encode(''.join([str(random.randint(0, 9)) for i in range(24)]))
    return nonce

def generateSignature(method, link, linkParameters, oauthParameters,
                      oauthConsumerSecret, oauthTokenSecret=None):
    '''
    Generate signature.
    '''

    if linkParameters:
        newDict = dict(oauthParameters, **linkParameters)
        params = urllib.urlencode(collections.OrderedDict(sorted(newDict.items())))
    else:
        params = urllib.urlencode(collections.OrderedDict(sorted(oauthParameters.items())))

    #Create your Signature Base String
    signatureBaseString = (method.upper()+'&'+percentEncode(str(link))+'&'+percentEncode(params))

    #Get the signing key
    signingKey = createSigningKey(oauthConsumerSecret, oauthTokenSecret)

    return calculateSignature(signingKey, signatureBaseString)



def calculateSignature(signingKey, signatureBaseString):
    '''
    Calculate signature using HMAC-SHA1 hashing algorithm.
    '''
    hashed = hmac.new(signingKey, signatureBaseString, hashlib.sha1)

    sig = binascii.b2a_base64(hashed.digest())[:-1]

    return percentEncode(sig)


def createSigningKey(oauthConsumerSecret, oauthTokenSecret):
    '''
    Creates a key to sign the request with.
    '''

    signingKey = percentEncode(oauthConsumerSecret) + '&' + percentEncode(oauthTokenSecret)

    return signingKey


def createAuthHeader(parameters):
    '''
    Format authorization header with oath parameters.
    '''

    orderedParameters = collections.OrderedDict(sorted(parameters.items()))
    authHeader = ('%s="%s"' % (k, v) for k, v in orderedParameters.iteritems())

    return "OAuth " + ', '.join(authHeader)


def getOauthParameters(consumerKey, accessToken):
    '''
    Returns parameters for making requests.
    '''
    oauthParameters = {
        'oauth_timestamp': str(int(time.time())),
        'oauth_signature_method': "HMAC-SHA1",
        'oauth_version': "1.0",
        'oauth_token': accessToken,
        'oauth_nonce': getNonce(),
        'oauth_consumer_key': consumerKey
    }

    return oauthParameters
