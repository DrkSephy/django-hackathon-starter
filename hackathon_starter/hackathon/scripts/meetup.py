'''
meetup.py aggregates various data from meetup.com.
'''

import requests
import simplejson as json

USERDATA = 'https://api.meetup.com/2/member/self/?access_token='

def retrieveUserData(url):
	req = requests.get(url)
	return req.content

