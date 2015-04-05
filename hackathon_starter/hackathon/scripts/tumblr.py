import requests
import simplejson as json
import time 
import urllib
import re
from bs4 import BeautifulSoup
import urlparse
import oauth2
from django.conf import settings

class TumblrOauthClient(object):
	request_token_url   = 'http://www.tumblr.com/oauth/request_token'
	authorize_url       = 'http://www.tumblr.com/oauth/authorize'
	access_token_url    = 'http://www.tumblr.com/oauth/access_token'
	user_uri			= "http://api.tumblr.com/v2/user/info"
	blog_uri			= "http://api.tumblr.com/v2/blog/"
	
	def __init__(self, consumer_key, consumer_secret, oauth_token='', oauth_token_secret='', oauth_verifier='', token=''):
		self.consumer_key = consumer_key
		self.cosnumer_secret = consumer_secret
		self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
		self.token = token
		self.oauth_token = oauth_token
		self.oauth_token_secret = oauth_token_secret
		self.oauth_verifier = oauth_verifier

	def get_authorize_url(self):
		client = oauth2.Client(self.consumer)
		resp, content = client.request(self.request_token_url, "GET")

		if int(resp['status']) != 200:
			raise Exception("Invalid response %s." % resp['status'])

		#parse content
		request_token = dict(urlparse.parse_qsl(content))
		self.oauth_token = request_token['oauth_token']
		self.oauth_token_secret = request_token['oauth_token_secret']

		#print authorize_url+"?oauth_token="+oauth_key+"&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/tumblr"
		return self.authorize_url+"?oauth_token="+self.oauth_token+"&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/tumblr"

	def get_access_token_url(self, oauth_verifier):
		#print "verifier"
		self.oauth_verifier = oauth_verifier
		token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
		token.set_verifier(self.oauth_verifier)

		client = oauth2.Client(self.consumer, token)
		resp, content = client.request(self.access_token_url,"POST")

		#print resp['status']

		access_token = dict(urlparse.parse_qsl(content))
		#print access_token

		#set verified token
		self.token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
		
	
	def getUserInfo(self):
		''' Returns users information. '''
		client = oauth2.Client(self.consumer, self.token)
		#print client
		resp, content = client.request(self.user_uri, "POST")
		if int(resp['status']) != 200:
			raise Exception("Invalid response %s." % resp['status'])

		#return content in json format
		jsonlist = json.loads(content)
		response = jsonlist['response']
		user_info = response['user']
		#print user_info
		return user_info

	def getBlogInfo(self, user):
		''' Returns blogger's blog information '''
		blog_info = self.blog_uri + user + ".tumblr.com/info?api_key="+self.consumer_key
		req = requests.get(blog_info)
		
		if int(req.status_code) != 200:
			raise Exception("Invalid response %s." % resp['status'])
		

		jsonlist = json.loads(req.content)
		response = jsonlist['response']
		blog 	 = response['blog']
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