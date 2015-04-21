import urlparse
import oauth2 as oauth
import requests
import base64, random

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

class TwitterOauthClient(object):

	oauth_token = None
	oauth_token_secret = None


	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
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
		'''

		client = oauth.Client(self.consumer)
		resp, content = client.request(request_token_url, 'GET')

		if int(resp['status']) != 200:
			raise Exception('Invalid response %s' %resp['status'])

		request_token = dict(urlparse.parse_qsl(content))

		#temporary
		self.oauth_token = request_token['oauth_token']
		self.oauth_token_secret  = request_token['oauth_token_secret']
		print self.oauth_token

		#link to authorize app access twitter data and return to twitter api example page
		link = authorize_url+"?oauth_token="+self.oauth_token+"&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/twitter/"
		return link

	def get_access_token_url(self, oauth_verifier):
		
		token = oauth.Token(self.oauth_token, self.oauth_token_secret)
		token.set_verifier(oauth_verifier)

		client = oauth.Client(self.consumer, token)
		resp, content = client.request(access_token_url, 'POST')
		
		if int(resp['status']) != 200:
			raise Exception('Invalid response %s' %resp['status'])

		print content
		access_token = dict(urlparse.parse_qsl(content))

		#permanent
		self.oauth_token = access_token['oauth_token']
		self.oauth_token_secret = access_token['oauth_token_secret']
		self.user_id = access_token['user_id']
		self.username = access_token['screen_name']


	def get_nonce(self):
		'''
		Unique token generated for each request.
		'''
		n = base64.b64encode(
			''.join([str(random.randint(0, 9)) for i in range(24)]))
		return n

	#def get_trends_available(self):

		





