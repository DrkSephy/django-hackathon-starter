import requests
import urllib
import simplejson as json

##########################
# FACEBOOK API CONSTANTS #
##########################

AUTHORIZE_URL = 'https://graph.facebook.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'
API_URL = 'https://graph.facebook.com/v2.3/'
REQUEST_PERMISSIONS_URL = "https://www.facebook.com/dialog/oauth?"

class FacebookOauthClient(object):
	'''
	Python client for Facebook API
	'''

	access_token = None
	permission_request_url = None

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


	

	def get_user_likes(self):
		'''
		Obtains a list of all the user likes. Require a special permission
		via Facebook.

		Returns:
			content: dictionary
				-A dictionary containing user likes.
		'''
		#Check if permission exists or ask for it
		if not self.check_permissions('user_likes'):
			requestedPermissionUrl = self.request_permissions('user_likes')

		#Get likes
		response = requests.get(API_URL + 'me/likes?access_token={at}'.format(at=self.access_token))
		return response.json()['data']
			


	def check_permissions(self, perm):
		'''
		Checks if the app has the specified permission.

		Parameters:
		    perm: String
		    	- The desired permission (such as user_likes)

		Returns:
			bool
				- True if the permission granted or false otherwise.
		'''

		permDict = {'status': 'granted', 'permission':perm}
		response = requests.get(API_URL + 'me/permissions?access_token={at}'.format(at=self.access_token))
		if response.status_code != 200:
			raise(Exception('Invalid response,response code: {c}'.format(c=response.status_code)))

		currentPermissions = response.json()['data']
		if permDict in currentPermissions:
			return True
		return False


	def request_permissions(self, perm):
		'''
			Requests a permission from the user.

			Parameters:
				perm: String
					- The permission we would like to get.

			Returns: String
				- The URL to redirect the user in order to get the permission.
		'''
		authSettings = {'client_id' : self.client_id, 
		                'redirect_uri' : 'http://localhost:8000/hackathon/', 
		                'auth_type' : 'rerequest', 
		                'scope' : perm,
		                'access_token' : access_token}
		params = urllib.urlencode(authSettings)
		self.permission_request_url = REQUEST_PERMISSIONS_URL + '?' + params
		