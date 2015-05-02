import requests
import simplejson as json
import time 
import urllib
import re
from bs4 import BeautifulSoup
import urlparse
import oauth2

request_token_url   = 'http://www.tumblr.com/oauth/request_token'
authorize_url       = 'http://www.tumblr.com/oauth/authorize'
access_token_url    = 'http://www.tumblr.com/oauth/access_token'

user_uri            = "http://api.tumblr.com/v2/user/info"
blog_uri            = "http://api.tumblr.com/v2/blog/"

class TumblrOauthClient(object):

    token = None
    oauth_verifier = None
    oauth_token = None
    oauth_token_secret = None
    accessed = False



    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        


    def authorize_url(self):
        client = oauth2.Client(self.consumer)
        resp, content = client.request(request_token_url, "GET")
        #parse content
        if not self.oauth_token:
            request_token = dict(urlparse.parse_qsl(content))
            self.oauth_token = request_token['oauth_token'] #'QBXdeeMKAnLzDbIG7dDNewTzRYyQoHZLbcn3bAFTCEFF5EXurl' #
            self.oauth_token_secret = request_token['oauth_token_secret']#'u10SuRl2nzS8vFK4K7UPQexAvbIFBFrZBjA79XDlgoXFxv9ZhO' #
        link = authorize_url+"?oauth_token="+self.oauth_token+"&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/tumblr"
        return link


    def access_token_url(self, oauth_verifier=''):
        self.accessed = True
        token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        self.oauth_verifier = oauth_verifier
        print self.oauth_verifier
        token.set_verifier(self.oauth_verifier)
        client = oauth2.Client(self.consumer, token)
        resp, content = client.request(access_token_url,"POST")
        access_token = dict(urlparse.parse_qsl(content))
        #set verified token
        self.token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
        #print self.token
            


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
        user_info = response['user']
        total_blogs = len(user_info['blogs'])
        #print user_info
        return user_info, total_blogs


    def getBlogInfo(self, user):
        ''' Returns blogger's blog information '''
        blog_info = blog_uri + user + ".tumblr.com/info?api_key="+self.consumer_key
        req = requests.get(blog_info)
        
        #if int(req.status_code) != 200:
        #   raise Exception("Invalid response %s." % resp['status'])
        

        jsonlist = json.loads(req.content)
        response = jsonlist['response']
        blog     = response['blog']
        blog['updated'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(blog['updated']))
        return blog


    def getTaggedInfo(self, tag):
        ''' Return tags related to blog with certain tag. '''

        tagged_uri = "http://api.tumblr.com/v2/tagged?tag="+tag+"&api_key="+self.consumer_key+"&limit=20"
        req = requests.get(tagged_uri)
        jsonlist = json.loads(req.content)

        tags = []

        meta = jsonlist['meta']
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
        
        tagged_uri = "http://api.tumblr.com/v2/tagged?tag="+tag+"&api_key="+self.consumer_key+"&limit=20"
        req = requests.get(tagged_uri)
        jsonlist = json.loads(req.content)
        
        meta = jsonlist['meta']
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
