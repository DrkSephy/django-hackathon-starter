# pylint: disable=invalid-name
# pylint: disable=too-many-instance-attributes

'''
tumblr.py contains methods for authenticating
the user via tumblr OAuth as well as methods
for getting data from Tumblr API.
'''


import requests
import simplejson as json
import time
import re
from bs4 import BeautifulSoup
import urlparse
import oauth2

request_token_url = 'http://www.tumblr.com/oauth/request_token'
authorize_url = 'http://www.tumblr.com/oauth/authorize'
access_token_url = 'http://www.tumblr.com/oauth/access_token'

user_uri = "http://api.tumblr.com/v2/user/info"
blog_uri = "http://api.tumblr.com/v2/blog/"

class TumblrOauthClient(object):
    '''
    Class responsible for authenticating the user
    via Tumblr OAuth2.
    '''
    token = None
    oauth_verifier = None
    oauth_token = None
    oauth_token_secret = None
    is_authorized = False
    access_token = None

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)

    def authorize_url(self):
        '''
        Redirects user to authorize use.
        '''
        client = oauth2.Client(self.consumer)
        resp, content = client.request(request_token_url, "GET")
        #parse content
        if not self.oauth_token:
            request_token = dict(urlparse.parse_qsl(content))
            self.oauth_token = request_token['oauth_token']
            self.oauth_token_secret = request_token['oauth_token_secret']
        link = authorize_url + "?oauth_token=" + self.oauth_token + \
            "&redirect_uri=http://127.0.0.1:8000/hackathon/"
        return link


    def access_token_url(self, oauth_verifier=''):
        '''
        Returns an access token to the user.
        '''
        self.is_authorized = True
        token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        self.oauth_verifier = oauth_verifier
        print self.oauth_verifier
        token.set_verifier(self.oauth_verifier)
        client = oauth2.Client(self.consumer, token)
        resp, content = client.request(access_token_url, "POST")
        self.access_token = dict(urlparse.parse_qsl(content))
        #set verified token
        self.token = oauth2.Token(self.access_token['oauth_token'], self.access_token['oauth_token_secret'])

    def getUserInfo(self):
        ''' Returns users information. '''
        client = oauth2.Client(self.consumer, self.token)
        #print client
        resp, content = client.request(user_uri, "POST")
        if int(resp['status']) != 200:
            raise Exception("Invalid response %s." % resp['status'])

        #return content in json format
        jsonlist = json.loads(content)
        response = jsonlist['response']
        self.username = str(response['user']['name'])
        user_info = response['user']
        total_blogs = len(user_info['blogs'])
        #print user_info
        return user_info, total_blogs


    def getBlogInfo(self, user):
        ''' Returns blogger's blog information '''
        blog_info = blog_uri + user + ".tumblr.com/info?api_key="+self.consumer_key
        req = requests.get(blog_info)
        jsonlist = json.loads(req.content)
        response = jsonlist['response']
        blog = response['blog']
        blog['updated'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(blog['updated']))
        return blog


    def getTaggedInfo(self, tag):
        ''' Return tags related to blog with certain tag. '''

        tagged_uri = "http://api.tumblr.com/v2/tagged?tag=" + tag + "&api_key=" + \
            self.consumer_key + "&limit=20"
        req = requests.get(tagged_uri)
        jsonlist = json.loads(req.content)
        tags = []
        body = jsonlist['response']
        for blog in body:
            for data in blog:
                if data == "tags":
                    #print blog[data]
                    for i in blog[data]:
                        m = re.match("(.*)(s*)s(t*)t(a*)a(r*)r(b*)b(u*)u(c*)c(k*)k(.*)", i.lower())
                        if not m:
                            tags.append(i)

        return tags


    def getTaggedBlog(self, tag):
        ''' Return the tagged blogs's captions or post.'''

        tagged_uri = "http://api.tumblr.com/v2/tagged?tag=" + tag + "&api_key=" + \
            self.consumer_key + "&limit=20"
        req = requests.get(tagged_uri)
        jsonlist = json.loads(req.content)
        body = jsonlist['response']

        tagtext = []

        for blog in body:
            #print "####"
            for data in blog:
                #post
                if data == "body":
                    if blog[data]:
                        #print blog[data]
                        soup = BeautifulSoup(blog[data])
                        text = soup.get_text()
                        tagtext.append(text)
                #an image
                if data == "caption":
                    if blog[data]:
                        #print blog[data]
                        soup = BeautifulSoup(blog[data])
                        text = soup.get_text()
                        tagtext.append(text)

        return tagtext
