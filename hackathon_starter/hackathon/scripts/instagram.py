
'''
instagram.py contains a handful of methods for interacting
with Instagram data and returning the responses as JSON.
'''

import requests
import urllib
import urllib2
import json
import simplejson as json2
import googlemaps
from django.conf import settings
from datetime import datetime
from time import strftime

authorization_url = 'https://api.instagram.com/oauth/authorize/?client_id='
access_token_url = 'https://api.instagram.com/oauth/access_token'

class InstagramOauthClient(object):
	'''
	Python Client for Instagram API.
	'''

	access_token = None
	user_data = None

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

		auth_url = authorization_url + self.client_id +'&redirect_uri=http://localhost:8000/hackathon/instagram&response_type=code'
		return auth_url


	def get_access_token(self, code):
		''' 
		Obtains access token.

		Parameters:
			code: String
				- The code is retrieved from the authorization url parameter
				  to obtain access_token.
		'''

		auth_setting = {'client_id': self.client_id,
						'client_secret': self.client_secret,
						'grant_type': 'authorization_code',
						'redirect_uri': 'http://localhost:8000/hackathon/instagram',
						'code': code
						}

		auth_setting_url =  urllib.urlencode(auth_setting)
		req  = urllib2.Request(access_token_url, auth_setting_url)
		content = urllib2.urlopen(req)
		jsonlist = json.load(content)
		self.access_token = jsonlist['access_token']
		self.user_data = jsonlist['user']
		#print self.user_data
		#print self.access_token


	def get_tagged_media(self, tag):
		'''
		Get recent tagged media.

		Parameters:
			tag: String
				- The tag used to search the most recent media that's tagged with it.

		Returns:
			data: Dictionary
				- A dictionary containing recent tagged 120 media counts data pertaining to each media.
		'''
		tagged_media_url = 'https://api.instagram.com/v1/tags/'+tag+'/media/recent?access_token='+self.access_token# +'&count=2'
		req = requests.get(tagged_media_url)
		content = json2.loads(req.content)
		data = content['data']

		while len(data) <= 100:
			next_url= content['pagination']['next_url']
			req = requests.get(next_url)
			content = json2.loads(req.content)
			for i in content['data']:
				data.append(i)
		print len(data)
		return data


	def get_user_info(self, access_token):
		'''
		Get user information.

		Parameters:
			access_token: String
				- The access_token given after granting permission
				  application access to Instagram data.

		Returns:
			data: Dictionary
				- A dictionary containing user information.
		'''

		user_info = 'https://api.instagram.com/v1/users/32833691/?access_token='+access_token
		req = requests.get(user_info)
		content = json2.loads(req.content)
		data = content['data']
		return data


	def get_user_media(self, access_token):
		'''
		Parameters:
			access_token: String
				- The access_token given after granting permission
				  application access to Instagram data.

		Returns:
			data: Dictionary
				- A dictionary containing user media information.
		'''

		user_media = 'https://api.instagram.com/v1/users/32833691/media/recent/?access_token='+access_token
		req = requests.get(user_media)
		content = json2.loads(req.content)
		data = content['data']
		return data

	def search_for_location(self, address, access_token):
		gmaps = googlemaps.Client(key=settings.GOOGLEMAP_API_KEY)
		#geocoding and address
		geocode_result = gmaps.geocode(address)
		
		if geocode_result:
			location = geocode_result[0]['geometry']['location']
			return location


	def search_location_ids(self, latitude, longitude, access_token):
		search_location = 'https://api.instagram.com/v1/locations/search?lat='+str(latitude)+'&lng='+str(longitude)+'&access_token='+access_token+"&distance=5000"
		req = requests.get(search_location)
		data = json2.loads(req.content)
		list_of_ids =[]
		if data['meta']['code'] != 200:
			raise Exception("Invalid response %s." % data['meta']['code'])
		search_ids = data['data']
		for data in search_ids:
			for i in data:
				if i == 'id':
					list_of_ids.append(data[i])
		return list_of_ids

	def search_location_media(self, list_location_ids, access_token):
		media = []
		for location in list_location_ids:
			media_by_location = 'https://api.instagram.com/v1/locations/'+location+'/media/recent?access_token='+access_token
			req = requests.get(media_by_location)
			content_all = json2.loads(req.content)
			if content_all['pagination']:
				temp_media=[]
				next_url = content_all['pagination']['next_url']
				req = requests.get(next_url)
				content = json2.loads(req.content)
				for i in content['data']:
					i['created_time'] = datetime.fromtimestamp(int(i['created_time'])).strftime('%Y-%m-%d %H:%M:%S')
					temp_media.append(i)
				media += [temp_media]
			else:
				for i in content_all['data']:
					for data in i:
						if data == 'created_time':
							i[data]= datetime.fromtimestamp(int(i[data])).strftime('%Y-%m-%d %H:%M:%S')
				media.append(content_all['data'])
		return media



