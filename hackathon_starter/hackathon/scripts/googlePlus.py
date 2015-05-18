import requests
import urllib
import simplejson as json
import random
import string


AUTHORISE_URL = 'https://accounts.google.com/o/oauth2/auth'
ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
REDIRECT_URL = 'http://localhost:8000/hackathon/'
PROFILE_API = 'https://www.googleapis.com/auth/plus.login'

class GooglePlus:

	access_token = None
	session_id = None

	def __init__(self, client_id, client_secret):
		'''
		Parameters:
			client_id: string
				- The client ID from the registering app on Google.

			client_secret: string
				-The client secret from the registering app on Google.
		'''
		self.client_id = client_id
		self.client_secret = client_secret


	def get_session_id(self, length=50):
		'''
		Generates a random session ID. As a part from the authentication process
		we need to verify that the response we get from the server contains the
		same session ID as we sent.

		Parameters:
			length: integer
				- The length of the session ID.
		'''
		chars = string.uppercase + string.digits + string.lowercase
		self.session_id = ''.join(random.choice(chars) for _ in range(length))


	def get_authorize_url(self):
		'''
		Obtains authorize url link with the given client_id.

		Returns:
			authURL: string
				- The authorization URL.
		'''

		self.get_session_id()
		authSettings = {'state': self.session_id, 
		                'redirect_uri':REDIRECT_URL,
		                'response_type':'code',
		                'client_id':self.client_id,
		                'scope': PROFILE_API}

		params = urllib.urlencode(authSettings)
		return AUTHORISE_URL + '?' + params


	def get_access_token(self, code, state):
		'''
		Obtains access token.

		Parameters:
			code: string
				- The code is retrived from the authorization URL parameter 
				to obtain access token.
			state: string
				- The unique session ID.
		'''

		#Checking that the sessino ID from the response match the session ID we sent
		if state != self.session_id:
			raise(Exception('Danger! Someone is messing up with you connection!'))

		authSettings = {'client_secret': self.client_secret,
		                'code':code,
		                'grant_type':'authorization_code', 
		                'client_id': self.client_id,
		                'redirect_uri': 'http://localhost:8000/hackathon/'}

		response = requests.post(ACCESS_TOKEN_URL, data=authSettings)
		if response.status_code != 200:
			raise(Exception('Invalid response, response code {c}'.format(c=response.status_code)))

		self.access_token = response.json()['access_token']



	def get_user_info(self):
		'''
		Obtain user information.

		Returns:
			content: dictionary
				- A dictionary contains user information.
		'''
		USER_INFO_API = 'https://www.googleapis.com/oauth2/v2/userinfo'
		params = urllib.urlencode({'access_token' : self.access_token})
		response = requests.get(USER_INFO_API + '?' + params)
		if response.status_code != 200:
			raise(Exception('Invalid response, response code {c}'.format(c=response.status_code)))

		return response.json()