'''
Module github.py contains a handful of methods
for interacting with Github data.
'''

import requests
import simplejson as json

########################
# GITHUB API CONSTANTS #
########################

API_BASE_URL = 'https://api.github.com/'
API_USERS_URL = API_BASE_URL + 'users/DrkSephy'

def getUserData():
	req = requests.get(API_USERS_URL)
	jsonList = []
	jsonList.append(json.loads(req.content))
	print jsonList
	
	
	
