import requests
import simplejson as json
import time 
import urllib
import re
from bs4 import BeautifulSoup
import urlparse
import oauth2

blog_uri		= "http://api.tumblr.com/v2/blog/"
user_uri		= "http://api.tumblr.com/v2/user/info"
request_token_url   = 'http://www.tumblr.com/oauth/request_token'
authorize_url       = 'http://www.tumblr.com/oauth/authorize'
access_token_url    = 'http://www.tumblr.com/oauth/access_token'

def simpleoauthurl(consumer_key, consumer_secret):
	#set consumer
	consumer = oauth2.Consumer(consumer_key, consumer_secret)

	#getting token
	client = oauth2.Client(consumer)
	resp, content = client.request(request_token_url, "GET")
	if int(resp['status']) != 200:
		raise Exception("Invalid response %s." % resp['status'])

	#parse content into dictionary
	request_token = dict(urlparse.parse_qsl(content))
	oauth_key = request_token['oauth_token']
	oauth_secret = request_token['oauth_token_secret']

	return authorize_url+"?oauth_token="+oauth_key+"&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/tumblr"


def getUserInfo(oauth_verifier):
	''' Return user's information. '''
	return "getUserInfo()"


def getBlogInfo(user, consumer_key):
	''' Return blogger's blog information.  '''
	blog_info = blog_uri + user +".tumblr.com/info?api_key="+consumer_key
	req = requests.get(blog_info)
	jsonlist = json.loads(req.content)
	
	meta = jsonlist['meta']
	response = jsonlist['response']
	blog = response['blog']
	blog['updated'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(blog['updated']))

	return blog

def getTaggedInfo(tag, consumer_key):
	''' Return tags related to blog with certain tag. '''

	tagged_uri = "http://api.tumblr.com/v2/tagged?tag="+tag+"&api_key="+consumer_key+"&limit=20"
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

def getTaggedBlog(tag, consumer_key):
	''' Return the tagged blogs's captions or post.'''
	
	tagged_uri = "http://api.tumblr.com/v2/tagged?tag="+tag+"&api_key="+consumer_key+"&limit=2"
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
