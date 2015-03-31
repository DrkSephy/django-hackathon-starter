import requests
import simplejson as json
import time 

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