import requests
import urllib
import simplejson as json
import pdb

##########################
# FACEBOOK API CONSTANTS #
##########################

AUTHORIZE_URL = 'https://graph.facebook.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'

class FacebookOauthClient(object):
	'''
	Python client for Facebook API
	'''

	access_token = None

	def __init__(self, client_id, client_secret):
		'''
		Parameters:
			client_id: String
				- The client id from the registering app on Facebook
			client_secret: String
				- The client secret from the registering app on Facebook
		'''
		self.client_id = client_id
		self.client_secret = client_secret



	def get_authorize_url(self):
		'''
		Obtains authorize url link with given client_id.

        Returns:
            authURL: String
                - The authorization url.

		'''
		authSettings = {'redirect_uri': "http://localhost:8000/hackathon/",
		                'client_id': self.client_id}
		params = urllib.urlencode(authSettings)
		return AUTHORIZE_URL + '?' + params



	def get_access_token(self, code):
		'''
		Obtains access token.

        Parameters:
            code: String
                - The code is retrieved from the authorization url parameter
                  to obtain access_token.
		'''
		authSettings = {'code': code,
		                'redirect_uri': "http://localhost:8000/hackathon/",
		                'client_secret': self.client_secret,
		                'client_id': self.client_id}
		params = urllib.urlencode(authSettings)
		response = requests.get(ACCESS_TOKEN_URL + '?' + params)

		if response.status_code != 200:
			raise(Exception('Invalid response,response code: {c}'.format(c=response.status_code)))

		response_array = str(response.text).split('&')
		self.access_token = str(response_array[0][13:])
		


	def get_user_info(self):
		'''
        Obtains user information.

        Returns:
            content: Dictionary
                - A dictionary containing user information.
		'''
		response = requests.get("https://graph.facebook.com/me?access_token={at}".format(at=self.access_token))
		if response.status_code != 200:
			raise(Exception('Invalid response,response code: {c}'.format(c=response.status_code)))

		return response.json()