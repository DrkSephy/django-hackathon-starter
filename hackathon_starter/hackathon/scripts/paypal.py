
'''
paypal.py contains a handful of methods for interacting
with Paypal data and returning the responses as JSON.
'''

import requests
import simplejson as json2
import unicodedata

authorization_url = 'https://www.sandbox.paypal.com/webapps/auth/protocol/openidconnect/v1/authorize?client_id='
access_token_url  = 'https://api.sandbox.paypal.com/v1/oauth2/token'

#password:testing123
#cafe.mui-buyer@gmail.com
#https://www.sandbox.paypal.com/webapps/auth/protocol/openidconnect/v1/authorize?client_id=AcOIP0f8NTl3iv5Etw2nakNrgPmjE65v84a2NQD5mm8-z-dTyhMSNHZuxHbHUaTAxLQIE0u-A2DFEY8M&response_type=code&scope=openid&redirect_uri=http://localhost:8000/hackathon/paypal/


class PaypalOauthClient(object):
	'''
	Python Client for Paypal API.
	'''

	access_token = None
	user_data = None
	token_type = None
	refresh_token = None

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

		self.client_id 		= client_id
		self.client_secret 	= client_secret


	def get_authorize_url(self):
		''' 
		Obtains authorize url link with given client_id.

		Returns:
			auth_url: String
				- The authorization url.
		'''

		auth_url = authorization_url + self.client_id + '&response_type=code&scope=openid&redirect_uri=http://localhost:8000/hackathon/paypal/'
		print auth_url
		return auth_url


	def get_access_token(self, code):
		''' 
		Obtains access token from authorization code.

		Parameters:
			code: String
				- The code is retrieved from the authorization url parameter
				  to obtain access_token.
		'''

		headers = {
					'Accept': 'application/json',
					'Accept-Language': 'en_US',
					'content-type': 'application/x-www-form-urlencoded'
				  }
		data = { 'grant_type': 'authorization_code',
				  'code': code,
				  'redirect_uri':'http://localhost:8000/hackathon/paypal'}


		req = requests.post(access_token_url, data=data, headers=headers, auth=(self.client_id, self.client_secret))
		
		if req.status_code != 200:
			raise Exception("Invalid response %s." %  req.status_code)
		
		content = unicodedata.normalize('NFKD', req.text).encode('ascii','ignore')
		jsonlist = json2.loads(content)

		#print jsonlist
		self.access_token = jsonlist['access_token']
		self.token_type = jsonlist['token_type']
		self.refresh_token = jsonlist['refresh_token']

		return self.refresh_token


	def get_refresh_token(self, refresh_token):
		'''
		This methods obtain new access token when current access_token expires.
		'''

		link  = 'https://api.sandbox.paypal.com/v1/identity/openidconnect/tokenservice'

		headers = {
					'Accept': 'application/json',
					'Accept-Language': 'en_US',
					'content-type': 'application/x-www-form-urlencoded'
				  }
		data = { 'grant_type': 'refresh_token',
				  'refresh_token': refresh_token}

		req = requests.post(link, data=data, headers=headers, auth=(self.client_id, self.client_secret))
		
		if req.status_code != 200:
			raise Exception("Invalid response %s." %  req.status_code)
		
		content = unicodedata.normalize('NFKD', req.text).encode('ascii','ignore')
		jsonlist = json2.loads(content)

		#print jsonlist
		self.access_token = jsonlist['access_token']
		self.token_type = jsonlist['token_type']
		return self.access_token


	def userinfo(self):
		link = 'https://api.sandbox.paypal.com/v1/identity/openidconnect/userinfo/?schema=openid'
		headers = { 'Content-Type':'application/json', 
				   'Authorization': self.token_type + ' '+ self.access_token,
				   'Accept-Language': 'en_US',
				   'content-type': 'application/x-www-form-urlencoded'
				 }
		req = requests.get(link, headers=headers)
		#print req.content

	