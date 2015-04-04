import requests
import simplejson as json
import time 
import urllib
import re
from bs4 import BeautifulSoup
import urlparse
import oauth2

blog_uri		= "http://api.tumblr.com/v2/blog/"
user_uri		= "api.tumblr.com/v2/user/"
consumer_key    = "KrSbAc9cYLmIgVAn1D21FjRR97QWsutNMxkPDFBxo8CMWtMk4M"
consumer_secret = "lKWMtL2Lj8zr5pY51PVqT8ugeoG0DjrdgoFewM0QTSyJ12jP8d"

#https://www.tumblr.com/oauth/authorize?oauth_token=R9HvkeqKgPAXjor9V92Zg5BvxMm3kwx0kaGnawVHIU5h6dmOL0

def getUserInfo():
	''' Return user's information. '''
	return "getUserInfo()"

def getBlogInfo(user):
	''' Return blogger's blog information.  '''

	blog_info = blog_uri + user +".tumblr.com/info?api_key="+consumer_key
	req = requests.get(blog_info)
	jsonlist = json.loads(req.content)
	print jsonlist
	
	meta = jsonlist['meta']
	response = jsonlist['response']
	blog = response['blog']
	blog['updated'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(blog['updated']))

	return blog

def getTaggedInfo(tag):
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

def getTaggedBlog(tag):
	''' Return the tagged blogs's captions or post.'''
	
	tagged_uri = "http://api.tumblr.com/v2/tagged?tag="+tag+"&api_key="+consumer_key+"&limit=2"
	req = requests.get(tagged_uri)
	jsonlist = json.loads(req.content)
	
	meta = jsonlist['meta']
	body = jsonlist['response']

	tagtext = []

	for blog in body:
		print "####"
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
