'''
Module github.py contains a handful of methods
for interacting with Github data.
'''

import requests
import simplejson as json

########################
# GITHUB API CONSTANTS #
########################

API_BASE_URL = 'https://api.github.com/users/DrkSephy'
#API_USERS_URL = API_BASE_URL + 'users/DrkSephy' + '?client_id=2404a1e21aebd902f6db' + '&client_secret=3da44769d4b7c9465fa4c812669148a163607c23'

def getUserData(clientID, clientSecret):
	'''Get generic Github User data.'''
	url = API_BASE_URL + clientID + clientSecret
	req = requests.get(url)
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
	

def getUserRepositories(clientID, clientSecret):
	'''Get a list of all repositories owned by a User.'''

	# Which page number of data are we looking at?
	pageNumber = 1

	# List of all our json
	jsonList = []

	# List of all repositories
	repositories = []

	# IDEA: Repeatedly loop over urls and check if the content has less than 30 entries.
	# 		If it does, then we have iterated over all the data. Time to parse it. 
	while True:
		req = requests.get('https://api.github.com/users/DrkSephy/repos?page=' + str(pageNumber) + '&client_id=2404a1e21aebd902f6db&client_secret=3da44769d4b7c9465fa4c812669148a163607c23')
		jsonList.append(json.loads(req.content))
		if len(json.loads(req.content)) < 30:
			break
		elif len(json.loads(req.content)) >= 30:
			pageNumber += 1

	# Loop over our data and extract all of the repository names
	for data in jsonList:
		for datum in data:
			repositories.append(datum['name'])

	return repositories

def getForkedRepositories(clientID, clientSecret):
	'''Get a list of all forked repositories by a user.'''
	# Which page number of data are we looking at?
	pageNumber = 1

	# List of all our json
	jsonList = []

	# List of all repositories
	forkedRepositories = []

	# IDEA: Repeatedly loop over urls and check if the content has less than 30 entries.
	# 		If it does, then we have iterated over all the data. Time to parse it. 
	while True:
		req = requests.get('https://api.github.com/users/DrkSephy/repos?page=' + str(pageNumber) + '&client_id=2404a1e21aebd902f6db&client_secret=3da44769d4b7c9465fa4c812669148a163607c23')
		jsonList.append(json.loads(req.content))
		if len(json.loads(req.content)) < 30:
			break
		elif len(json.loads(req.content)) >= 30:
			pageNumber += 1

	# Loop over our data and extract all of the repository names
	forkedRepos = {}
	for data in jsonList:
		for datum in data:
			if datum['fork'] == True:
				#print datum['name']
				forkedRepos['name'] = datum['name']
				forkedRepositories.append(forkedRepos)
				forkedRepos = {}

	return forkedRepositories

def getTopContributedRepositories(repos, clientID, clientSecret):
	'''Get a list of all commits for each repository owned.'''

	jsonList = []
	for repo in repos:
		# print repo
		req = requests.get('https://api.github.com/repos/DrkSephy/' + repo + '/stats/contributors' + clientID + clientSecret)
		jsonList.append(json.loads(req.content))

	parsedData = []
	# Keep track of which JSON set we are processing to get the repo name
	indexNumber = -1
	for item in jsonList:
		indexNumber += 1
		commits = {}
		for data in item:
			if data['author']['login'] == 'DrkSephy':
				commits['author'] = data['author']['login']
				commits['total'] = data['total']
				commits['repo_name'] = repos[indexNumber]
				parsedData.append(commits)

	return parsedData

def filterCommits(data):
	'''Returns the top 10 committed repositories.'''

	maxCommits = []
	for i in range(1, 10):
		maxCommitedRepo = max(data, key=lambda x:x['total'])
		maxCommits.append(maxCommitedRepo)
		index = data.index(maxCommitedRepo)
		data.pop(index)
	return maxCommits
	
	
def getStarGazerCount(clientID, clientSecret):
	'''Get Stargazer counts for all repositories.'''

	# Which page number of data are we looking at?
	pageNumber = 1

	# List of all our json
	jsonList = []

	# List of all repositories
	stargazers = []

	# IDEA: Repeatedly loop over urls and check if the content has less than 30 entries.
	# 		If it does, then we have iterated over all the data. Time to parse it. 
	while True:
		req = requests.get('https://api.github.com/users/DrkSephy/repos?page=' + str(pageNumber) + '&client_id=2404a1e21aebd902f6db&client_secret=3da44769d4b7c9465fa4c812669148a163607c23')
		jsonList.append(json.loads(req.content))
		if len(json.loads(req.content)) < 30:
			break
		elif len(json.loads(req.content)) >= 30:
			pageNumber += 1

	# Loop over our data and extract all of the repository names
	for data in jsonList:
		for datum in data:
			starData = {}
			starData['stargazers_count'] = datum['stargazers_count']
			starData['name'] = datum['name']
			stargazers.append(starData)

	return stargazers

def filterStarGazerCount(data):
	'''Return top 10 starred repositories.'''
	maxStars= []
	for i in range(1, 10):
		maxStarGazers = max(data, key=lambda x:x['stargazers_count'])
		maxStars.append(maxStarGazers)
		index = data.index(maxStarGazers)
		data.pop(index)
	return maxStars





