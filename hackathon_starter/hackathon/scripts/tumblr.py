import requests
import simplejson as json
import time 
import collections
import urllib
import re
from bs4 import BeautifulSoup
#from textblob.sentiments import NaiveBayesAnalyzer
#from textblob import TextBlob

###starbucks how they feel?
#google tumblr hackathon ideas
#sentian analysis
blog_uri		= "http://api.tumblr.com/v2/blog/"
user_uri		= "api.tumblr.com/v2/user/"
consumer_key    = "KrSbAc9cYLmIgVAn1D21FjRR97QWsutNMxkPDFBxo8CMWtMk4M"
consumer_secret = "lKWMtL2Lj8zr5pY51PVqT8ugeoG0DjrdgoFewM0QTSyJ12jP8d"
oauth_token		= "b2osMdhLljOo5aVBjd47kU7gm08NSTqZnZa1b6gC8MmpZX8h0H"
oauth_secret	= "jHsrI4qM5h4CbUre90SZRAG6snguY22tB1NdujgAZwFh8VD1B1"

def getUserInfo():
	return "getUserInfo()"

def getBlogInfo(user):
	blog_info = blog_uri + user +".tumblr.com/info?api_key="+consumer_key
	req = requests.get(blog_info)
	jsonlist = json.loads(req.content)
	
	meta = jsonlist['meta']
	response = jsonlist['response']
	blog = response['blog']
	blog['updated'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(blog['updated']))

	return meta, response, blog

def getTaggedInfo(tag):
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