

import urllib
import urlparse
import oauth2 as oauth
import simplejson



class LinkedInAPI(object):
    
    base_url = 'https://api.linkedin.com'
    li_url ='http://www.linkedin.com'


    api_profile_connections_url = base_url + '/v1/people/~/connections'
    api_profile_url = base_url + '/v1/people/~'
    

    access_token_path = base_url + '/uas/oauth/accessToken'
    authorize_path = base_url + '/uas/oauth/authorization'
   

    def __init__(self, ck, cs, ut, us):
        self.consumer_key = ck
        self.consumer_secret = cs
        self.user_token = ut
        self.user_secret = us
        self.consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)

    def get_authorize_url(self):

         li_url ='http://www.linkedin.com'
         authorize_path = li_url +'/uas/oauth/authorization'
         auth_url = authorize_path+'?response_type=code'+self.consumer_key+'redirect_uri=https://127.0.0.1:8000/hackathon/linkedin'
         return auth_url

    def get_access_token(self, request_token, verifier):

        token = self.get_user_token(request_token)
        token.set_verifier(verifier)
        return dict(urlparse.parse_qsl(self.request(
            self.access_token_path, {}, 'POST', token=token)))

    

    def get_user_connections(self, access_token, selectors=None, query_args=None, headers=None):
   
        token = self.get_user_token(access_token)
        url = self.api_profile_connections_url
        if selectors:
            assert type(selectors) == type([]), (
                '"Keyword argument "selectors" must be of type "list"')
            url = self.prepare_field_selectors(selectors, url)
        return simplejson.loads(self.request(
            url, query_args, 'GET', headers=headers, token=token))

    def get_user_profile(self, access_token, selectors=None, headers=None, **query_args):
        token = self.get_user_token(access_token)
        url = self.api_profile_url
        if selectors:
            assert type(selectors) == type([]), (
                '"Keyword argument "selectors" must be of type "list"')
            url = self.prepare_field_selectors(selectors, url)
        return simplejson.loads(self.request(
            url, query_args, 'GET', token=token, headers=headers))

    