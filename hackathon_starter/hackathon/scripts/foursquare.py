import simplejson as json
import urllib
import requests


############################
# FOURSQUARE API CONSTANTS #
############################
AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'
REDIRECT_URL = 'http://localhost:8000/hackathon'


class FoursquareOauthClient(object):
    '''
    Pytohn client for Foursquare API
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
        authSettings = {'client_id': self.client_id,
                        'response_type': 'code',
                        'redirect_uri': REDIRECT_URL}

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

        authSettings = {'client_id': self.client_id,
                        'client_secret': self.client_secret,
                        'grant_type': 'authorization_code',
                        'redirect_uri': REDIRECT_URL,
                        'code': code}

        params = urllib.urlencode(authSettings)
        response = requests.get(ACCESS_TOKEN_URL + '?' + params)

        if response.status_code != 200:
			raise(Exception('Invalid response,response code: {c}'.format(c=response.status_code)))

        self.access_token = response.json()['access_token']


    def get_user_info(self, api_version='20140806'):
        '''
        Obtains user information.

        Parameters:
            api_version: string
                - The API version you would use. This parameter is mandatory by Foursquare.

        Returns:
            content: Dictionary
                - A dictionary containing user information.
		'''
        USER_INFO_API_URL = 'https://api.foursquare.com/v2/users/self'

        authSettings={'v':api_version,
                      'oauth_token': self.access_token}

        params = urllib.urlencode(authSettings)

        response = requests.get(USER_INFO_API_URL + '?' + params)

        if response.status_code != 200:
			raise(Exception('Invalid response,response code: {c}'.format(c=response.status_code)))

        return response.json()['response']['user']
