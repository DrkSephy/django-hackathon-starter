
'''
twitter.py contains a handful of methods for interacting
with Twitter data and returning the responses as JSON.
'''


import urlparse
import oauth2 as oauth
import requests
import base64, random
import urllib
import binascii
import time, collections, json, hmac, hashlib
import simplejson as json2

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

class TwitterOauthClient(object):
	'''
	Python Client for Twitter API.
	'''	

	oauth_token = None
	oauth_token_secret = None


	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
		'''
		Parameters:
			consumer_key: String
				- The consumer_key from registering application
				  on Instagram.
			consumer_secret: String
				- The consumer_secret from registering application
				  on Instagram.
		'''		
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




	def get_trends_available(self, yahoo_consumer_key):
		method = "get"
		link = 'https://api.twitter.com/1.1/trends/available.json'
		link_parameters = {}
		#link = 'https://api.twitter.com/1.1/trends/closest.json'
		#link_parameters = {'lat':'40.782032', 'long':'-73.9717188'}
		#link = 'https://api.twitter.com/1.1/trends/place.json'
		#link_parameters = {'id': '1'}
		

		oauth_parameters = get_oauth_parameters(
		    self.consumer_key,
		    self.access_token
		)

		oauth_parameters['oauth_signature'] = generate_signature(
		    method,
		    link,
		    link_parameters,
		    oauth_parameters,
		    self.consumer_key,
		    self.consumer_secret,
		    self.access_token_secret
		)

		headers = {'Authorization': create_auth_header(oauth_parameters)}

		if link_parameters:
			link += '?'+urllib.urlencode(link_parameters)

		req = requests.get(link, headers=headers)
		#print req.status_code
		
		if int(req.status_code) != 200:
			raise Exception('Invalid response %s' %req.status_code)

		content = json2.loads(req.content)
		#print len(content)
		
		for place in content:
			for e in place:
				if e == 'url':
					request_neighbor_data=  requests.get(place[e]+'/neighbors?appid='+yahoo_consumer_key+'&format=json')
					#print request_neighbor_data.status_code
					if request_neighbor_data.status_code == 200:
						neighbor = json2.loads(request_neighbor_data.content)
					else:
						neighbor = {}

			place['neighbor'] = neighbor
					#print place


		return content
		




def percent_encode(string):
	'''
	Percent encode strings.
	'''
	return urllib.quote(string, safe='~')


def get_nonce():
	'''
	Generate unique token per request.
	'''

	n = base64.b64encode(''.join([str(random.randint(0, 9)) for i in range(24)]))
	return n


def generate_signature(method, link, link_parameters, oauth_parameters, oauth_consumer_key, oauth_consumer_secret, oauth_token_secret=None, status=None):
    '''
    Generate signature.
    '''
    if link_parameters:
    	new_dict = dict(oauth_parameters, **link_parameters)
    	parameters = urllib.urlencode(collections.OrderedDict(sorted(new_dict.items())))
    else:
    	parameters = urllib.urlencode(collections.OrderedDict(sorted(oauth_parameters.items())))

    #Create your Signature Base String
    signature_base_string = ( method.upper() + '&' + percent_encode(str(link)) + '&' + percent_encode(parameters))

    #Get the signing key
    signing_key = create_signing_key(oauth_consumer_secret, oauth_token_secret)

    return calculate_signature(signing_key, signature_base_string)



def calculate_signature(signing_key, signature_base_string):
    '''
    Calculate signature using HMAC-SHA1 hashing algorithm.
    '''
    hashed = hmac.new(signing_key, signature_base_string, hashlib.sha1)

    sig = binascii.b2a_base64(hashed.digest())[:-1]

    return percent_encode(sig)


def create_signing_key(oauth_consumer_secret, oauth_token_secret):
    '''
    Creates a key to sign the request with.
    '''

    signing_key = percent_encode(oauth_consumer_secret) + '&' + percent_encode(oauth_token_secret)

    return signing_key


def create_auth_header(parameters):
	'''
	Format authorization header with oath parameters.
	'''

	ordered_parameters = collections.OrderedDict(sorted(parameters.items()))
	auth_header = ('%s="%s"' % (k, v) for k, v in ordered_parameters.iteritems())

	return "OAuth " + ', '.join(auth_header)


def get_oauth_parameters(consumer_key, access_token):
    '''
    Returns parameters for making requests.
    '''
    oauth_parameters = {
        'oauth_timestamp': str(int(time.time())),
        'oauth_signature_method': "HMAC-SHA1",
        'oauth_version': "1.0",
        'oauth_token': access_token,
        'oauth_nonce': get_nonce(),
        'oauth_consumer_key': consumer_key
    }

    return oauth_parameters

    