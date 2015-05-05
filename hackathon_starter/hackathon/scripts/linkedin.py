

import simplejson as json
import requests
import urlparse, urllib

AUTHORIZATION_URL = 'https://www.linkedin.com/uas/oauth2/authorization'
ACCESS_TOKEN_URL = 'https://www.linkedin.com/uas/oauth2/accessToken'

class LinkedinOauthClient(object):

    is_authorized = False

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_authorize_url(self):
        auth_setting = {'response_type' : 'code',
                        'client_id' : self.client_id,
                        'client_secret' : self.client_secret,
                        'redirect_uri' : 'http://127.0.0.1:8000/hackathon/',
                        'state' : 'DCEeFWf45A53sdfKef424',
                        'scope': 'r_basicprofile'}

        params = urllib.urlencode(auth_setting)
        authURL = AUTHORIZATION_URL + '?' + params
        return authURL

    def get_access_token(self, code):
        settings = {'grant_type' : 'authorization_code',
                    'code' : code,
                    'redirect_uri' : 'http://127.0.0.1:8000/hackathon/',
                    'client_id' : self.client_id,
                    'client_secret': self.client_secret}

        header = {'content-type' : 'application/x-www-form-urlencoded'}
        params = urllib.urlencode(settings)
        link = ACCESS_TOKEN_URL + '?' + params
        req = requests.post(link)#, headers=header)

        if req.status_code != 200:
            raise Exception('Invalid response %s' %req.status_code)

        content = json.loads(req.content)
        self.access_token = content['access_token']
        self.is_authorized = True
