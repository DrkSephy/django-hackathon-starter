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
API_USERS_URL = API_BASE_URL + 'users/DrkSephy' + '?client_id=2404a1e21aebd902f6db' + '&client_secret=3da44769d4b7c9465fa4c812669148a163607c23'

# Endpoint to get statistics in a repository
# https://api.github.com/repos/DrkSephy/WaterEmblem/stats/contributors
# https://api.github.com/repos/:user/:repo/stats/contributors

def getUserData():
	req = requests.get(API_USERS_URL)
	jsonList = []
	jsonList.append(json.loads(req.content))
	parsedData = []
	userData = {}
	for data in jsonList: 
		userData['name'] = data['name']
		userData['blog'] = data['blog']
		userData['email'] = data['email']
		userData['public_gists'] = data['public_gists']
		userData['public_repos'] = data['public_repos']
		userData['avatar_url'] = data['avatar_url']
		userData['followers'] = data['followers']
		userData['following'] = data['following']
	parsedData.append(userData)

	return parsedData
	

def getUserRepositories():
	pageNumber = 1
	firstUrl = API_USERS_URL + '/repos' + '?page=' + str(pageNumber) + '&client_id=2404a1e21aebd902f6db' + '&client_secret=3da44769d4b7c9465fa4c812669148a163607c23'
	urls = []
	urls.append(firstUrl)
	jsonList = []
	repositories = []
	while True:
		req = requests.get(API_USERS_URL + '/repos' + '?page=' + str(pageNumber) + '&client_id=2404a1e21aebd902f6db' + '&client_secret=3da44769d4b7c9465fa4c812669148a163607c23')
		jsonList.append(json.loads(req.content))
		for data in jsonList:
			for datum in data:
				if len(datum) < 30:
					print 'hello'
					break
				elif len(datum) >= 30:
					pageNumber += 1
					urls.append(API_USERS_URL + '/repos' + '?page=' + str(pageNumber) + '&client_id=2404a1e21aebd902f6db' + '&client_secret=3da44769d4b7c9465fa4c812669148a163607c23')
	print urls
	
	return repositories

	
	
