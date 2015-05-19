import simplejson as json
import urllib
import requests
import string
import pdb
import random


AUTHORIZE_URL = 'https://www.dropbox.com/1/oauth2/authorize'
ACCESS_TOKEN_URL = 'https://api.dropbox.com/1/oauth2/token'


class DropboxOauthClient(object):

	access_token = None
	session_id = None
	def __init__(self, client_id, client_secret):
		self.client_id = client_id
		self.client_secret = client_secret


	def get_authorize_url(self):
		self.get_session_id()
		authSettings = {'response_type': 'code',
		                'client_id': self.client_id,
		                'redirect_uri': 'http://localhost:8000/hackathon',
		                'state': self.session_id}

		params = urllib.urlencode(authSettings)

		return AUTHORIZE_URL + '?' + params

	def get_session_id(self, length=50):
		chars = string.uppercase + string.digits + string.lowercase
		self.session_id = ''.join(random.choice(chars) for _ in range(length))

	def get_access_token(self, code, state):
		if state != self.session_id:
			raise(Exception('Danger! Someone is messing up with you connection!'))

		authSettings = {'code': code,
		                'grant_type': 'authorization_code',
		                'client_id': self.client_id,
		                'client_secret': self.client_secret,
		                'redirect_uri': 'http://localhost:8000/hackathon'}

		response = requests.post(ACCESS_TOKEN_URL, data=authSettings)

		if response.status_code!=200:
			raise(Exception('Invalid response, response code {c}'.format(c=response.status_code)))
		self.access_token = response.json()['access_token']


	def get_user_info(self):
		USER_INFO_API = 'https://api.dropbox.com/1/account/info'
		params = urllib.urlencode({'access_token': self.access_token})
		response = requests.get(USER_INFO_API + '?' + params)
		if response.status_code!=200:
			raise(Exception('Invalid response, response code {c}'.format(c=response.status_code)))
		return response.json()
