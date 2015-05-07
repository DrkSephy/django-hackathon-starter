import unittest
from mock import Mock, patch, MagicMock
from django.conf import settings
from hackathon.scripts.github import getUserData, getUserRepositories, getForkedRepositories, getTopContributedRepositories, getStarGazerCount, filterStarGazerCount, filterCommits


class GithubTests(unittest.TestCase):

	def setUp(self):
		self.API_BASE_URL = 'https://api.github.com/users/DrkSephy'
		self.clientID = 'client_id=2404a1e21aebd902f6db'
		self.clientSecret = 'client_secret=3da44769d4b7c9465fa4c812669148a163607c23'

	
	def testGetUserData(self):
		'''Test for github.py getUserData method'''

		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		user = 'DrkSephy'

		# Construct the URL
		self.url = self.API_BASE_URL +  '?' + clientID + '&' + clientSecret

		# Instantiate data collection objects
		jsonList = []
		parsedData = []
		userData = {}

		with patch('hackathon.scripts.github.getUserData') as mock_getUserData:
			# Mock the return value of this method
			#mock_getUserData.return_value = {'public_repos': 50, 'public_gists': 5, 'name': 'David Leonard', 'blog': 'http://drksephy.github.io', 'avatar_url': 'https://avatars.githubusercontent.com/u/1226900?v=3', 'followers': 52, 'following': 7, 'email': 'DrkSephy1025@gmail.com'}
			mock_getUserData.return_value = getUserData(user, clientID, clientSecret)
			#print 'Yeah?'
			#print mock_getUserData.return_value
			#print mock_getUserData.return_value[0]['public_repos']

			for data in mock_getUserData.return_value:				
				userData['name'] = data['name']
				userData['blog'] = data['blog']
				userData['email'] = data['email']
				userData['public_gists'] = data['public_gists']
				userData['public_repos'] = data['public_repos']
				userData['avatar_url'] = data['avatar_url']
				userData['followers'] = data['followers']
				userData['following'] = data['following']
				
			parsedData.append(userData)
			self.assertEqual(getUserData(user, clientID, clientSecret), parsedData)

	def testGetUserRepositories(self):
		'''Test for github.py getUserRepositories'''

		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		user = 'DrkSephy'

		pageNumber = 1
		jsonList = []
		repositories = []
		while True:
			with patch('hackathon.scripts.github.getUserRepositories') as mock_getUserRepositories:
				mock_getUserRepositories.return_value = { "id": 22388667, "name": "ACM-Game-Presentation" }	
				jsonList.append(mock_getUserRepositories.return_value)
				if len(mock_getUserRepositories.return_value) < 30:
					break
				elif len(mock_getUserRepositories.return_value) >= 30:
					pageNumber += 1


		repositories = getUserRepositories(user, clientID, clientSecret)

		self.assertEqual(getUserRepositories(user, clientID, clientSecret), repositories)


	def testGetForkedRepositories(self):
		'''Test for github.py getForkedRepositories'''

		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		user = 'DrkSephy'
		
		pageNumber = 1
		jsonList = []
		forkedRepositories = []

		while True:
			with patch('hackathon.scripts.github.getUserRepositories') as mock_getForkedRepositories:
				mock_getForkedRepositories.return_value = { "id": 22388667, "name": "ACM-Game-Presentation" }	
				jsonList.append(mock_getForkedRepositories.return_value)
				if len(mock_getForkedRepositories.return_value) < 30:
					break
				elif len(mock_getForkedRepositories.return_value) >= 30:
					pageNumber += 1

		forkedRepositories = [{'name': 'async'}, {'name': 'FizzBuzz-Test-1'}, {'name': 'hackathon-starter'}, {'name': 'historicalWeather'}, {'name': 'jsrecipes'}, {'name': 'node'}, {'name': 'rst2pdf'}, {'name': 'rust-by-example'}, {'name': 'satellizer'}, {'name': 'vitanao'}, {'name': 'WaterEmblem'}, {'name': 'webauth-via-ssh'}]
		self.assertEqual(getForkedRepositories(user, clientID, clientSecret), forkedRepositories)

	def testGetTopContributedRepositories(self):
		'''Test for github.py getTopContributedRepositories'''
		
		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		repos = ['async']
		user = 'DrkSephy'

		jsonList = []
		for repo in repos:
			with patch('hackathon.scripts.github.getTopContributedRepositories') as mock_getTopContributedRepositories:
				mock_getTopContributedRepositories.return_value = [{'total': 85, 'repo_name': 'ACM-Game-Presentation', 'author': 'DrkSephy'}, 
																	{'total': 16, 'repo_name': 'ACM-Portfolio-Presentation', 'author': 'DrkSephy'}, 
																	{'total': 17, 'repo_name': 'angular-nhl', 'author': 'DrkSephy'}, 
																	{'total': 1, 'repo_name': 'async', 'author': 'DrkSephy'}, 
																	{'total': 55, 'repo_name': 'd3-sandbox', 'author': 'DrkSephy'}, 
																	{'total': 7, 'repo_name': 'Deep-Learning', 'author': 'DrkSephy'}, 
																	{'total': 11, 'repo_name': 'Django-Hackathon-Starter', 'author': 'DrkSephy'}, 
																	{'total': 433, 'repo_name': 'drksephy.github.io', 'author': 'DrkSephy'}, 
																	{'total': 3, 'repo_name': 'el-gamal-attack', 'author': 'DrkSephy'}, 
																	{'total': 1, 'repo_name': 'FizzBuzz-Test-1', 'author': 'DrkSephy'}, 
																	{'total': 44, 'repo_name': 'flux-reactJS', 'author': 'DrkSephy'}, 
																	{'total': 4, 'repo_name': 'fractals', 'author': 'DrkSephy'}]
				jsonList.append(mock_getTopContributedRepositories.return_value)


		parsedData = []
		indexNumber = -1
		for entry in jsonList:
			indexNumber += 1
			commits = {}
			for item in entry:
				if item['author'] == 'DrkSephy':
					commits['author'] = item['author']
					commits['total'] = item['total']
					commits['repo_name'] = item['repo_name']
					parsedData.append(commits)

		parsedData = [{'total': 1, 'repo_name': 'async', 'author': 'DrkSephy'}]

		
		self.assertEqual(getTopContributedRepositories(user, repos, clientID, clientSecret), parsedData)


	def testGetStarGazerCount(self):
		'''Test for github.py getStarGazerCount'''

		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		user = 'DrkSephy'

		pageNumber = 1
		jsonList = []
		stargazers = []

		while True:
			with patch('hackathon.scripts.github.getStarGazerCount') as mock_getStarGazerCount:
				mock_getStarGazerCount.return_value = { "id": 22388667, "name": "ACM-Game-Presentation" }	
				jsonList.append(mock_getStarGazerCount.return_value)
				if len(mock_getStarGazerCount.return_value) < 30:
					break
				elif len(mock_getStarGazerCount.return_value) >= 30:
					pageNumber += 1

		stargazers = getStarGazerCount(user, clientID, clientSecret)
		self.assertEqual(getStarGazerCount(user, clientID, clientSecret), stargazers)



	def testFilterStarGazerCount(self):
		'''Test for github.py filterStarGazerCount'''
		maxStars = []
		data = [{'stargazers_count': 0, 'name': 'ACM-Game-Presentation'}, {'stargazers_count': 1, 'name': 'ACM-Portfolio-Presentation'}, {'stargazers_count': 2, 'name': 'angular-nhl'}, {'stargazers_count': 0, 'name': 'async'}, {'stargazers_count': 0, 'name': 'd3-sandbox'}, {'stargazers_count': 3, 'name': 'Deep-Learning'}, {'stargazers_count': 0, 'name': 'Django-Hackathon-Starter'}, {'stargazers_count': 0, 'name': 'drksephy.github.io'}, {'stargazers_count': 0, 'name': 'el-gamal-attack'}, {'stargazers_count': 0, 'name': 'FizzBuzz-Test-1'}, {'stargazers_count': 0, 'name': 'flux-reactJS'}, {'stargazers_count': 0, 'name': 'fractals'}, {'stargazers_count': 0, 'name': 'git-api'}, {'stargazers_count': 1, 'name': 'git-technetium'}, {'stargazers_count': 0, 'name': 'hackathon-starter'}, {'stargazers_count': 0, 'name': 'hackcity'}, {'stargazers_count': 0, 'name': 'hackcity.github.io'}, {'stargazers_count': 0, 'name': 'historicalWeather'}, {'stargazers_count': 0, 'name': 'I4330'}, {'stargazers_count': 1, 'name': 'integrated-chinese'}, {'stargazers_count': 0, 'name': 'jsrecipes'}, {'stargazers_count': 0, 'name': 'learn-angularJS'}, {'stargazers_count': 1, 'name': 'legionJS'}, {'stargazers_count': 0, 'name': 'lehman-hackathon'}, {'stargazers_count': 0, 'name': 'mean-sandbox'}, {'stargazers_count': 0, 'name': 'mean-stack-talk'}, {'stargazers_count': 2, 'name': 'NOAA-Projects'}, {'stargazers_count': 0, 'name': 'node'}, {'stargazers_count': 0, 'name': 'nodeapps'}, {'stargazers_count': 1, 'name': 'pascal-compiler'}, {'stargazers_count': 0, 'name': 'pascal-js'}, {'stargazers_count': 0, 'name': 'Project-Euler'}, {'stargazers_count': 0, 'name': 'python-imp-interpreter'}, {'stargazers_count': 0, 'name': 'rst2pdf'}, {'stargazers_count': 0, 'name': 'rust-by-example'}, {'stargazers_count': 1, 'name': 'rust-sandbox'}, {'stargazers_count': 0, 'name': 'satellizer'}, {'stargazers_count': 0, 'name': 'smw-asm'}, {'stargazers_count': 2, 'name': 'swift-sandbox'}, {'stargazers_count': 1, 'name': 'Tales-of-Kratos'}, {'stargazers_count': 0, 'name': 'theano-sandbox'}, {'stargazers_count': 0, 'name': 'todo'}, {'stargazers_count': 0, 'name': 'TV-Show-Premieres'}, {'stargazers_count': 0, 'name': 'tv-show-tracker'}, {'stargazers_count': 0, 'name': 'vitanao'}, {'stargazers_count': 0, 'name': 'WaterEmblem'}, {'stargazers_count': 0, 'name': 'webauth-ssh-authentication'}, {'stargazers_count': 0, 'name': 'webauth-via-ssh'}, {'stargazers_count': 0, 'name': 'WebRing'}, {'stargazers_count': 0, 'name': 'yabe'}]
		with patch('hackathon.scripts.github.filterStarGazerCount') as mock_filterStarGazerCount:
			mock_filterStarGazerCount.return_value = [{'stargazers_count': 3, 'name': 'Deep-Learning'}, {'stargazers_count': 2, 'name': 'angular-nhl'}, {'stargazers_count': 2, 'name': 'NOAA-Projects'}, {'stargazers_count': 2, 'name': 'swift-sandbox'}, {'stargazers_count': 1, 'name': 'ACM-Portfolio-Presentation'}, {'stargazers_count': 1, 'name': 'git-technetium'}, {'stargazers_count': 1, 'name': 'integrated-chinese'}, {'stargazers_count': 1, 'name': 'legionJS'}, {'stargazers_count': 1, 'name': 'pascal-compiler'}]
			maxStars = filterStarGazerCount(data)
			self.assertEqual(maxStars, maxStars)

	def testFilterCommits(self):
		'''Test for github.py filtercommits'''
		maxCommits = []
		data = [{'total': 85, 'repo_name': 'ACM-Game-Presentation', 'author': 'DrkSephy'}, {'total': 16, 'repo_name': 'ACM-Portfolio-Presentation', 'author': 'DrkSephy'}, {'total': 17, 'repo_name': 'angular-nhl', 'author': 'DrkSephy'}, {'total': 1, 'repo_name': 'async', 'author': 'DrkSephy'}, {'total': 55, 'repo_name': 'd3-sandbox', 'author': 'DrkSephy'}, {'total': 7, 'repo_name': 'Deep-Learning', 'author': 'DrkSephy'}, {'total': 11, 'repo_name': 'Django-Hackathon-Starter', 'author': 'DrkSephy'}, {'total': 433, 'repo_name': 'drksephy.github.io', 'author': 'DrkSephy'}, {'total': 3, 'repo_name': 'el-gamal-attack', 'author': 'DrkSephy'}, {'total': 1, 'repo_name': 'FizzBuzz-Test-1', 'author': 'DrkSephy'}, {'total': 44, 'repo_name': 'flux-reactJS', 'author': 'DrkSephy'}, {'total': 4, 'repo_name': 'fractals', 'author': 'DrkSephy'}, {'total': 32, 'repo_name': 'git-api', 'author': 'DrkSephy'}, {'total': 160, 'repo_name': 'git-technetium', 'author': 'DrkSephy'}, {'total': 1, 'repo_name': 'hackathon-starter', 'author': 'DrkSephy'}, {'total': 6, 'repo_name': 'hackcity', 'author': 'DrkSephy'}, {'total': 4, 'repo_name': 'hackcity.github.io', 'author': 'DrkSephy'}, {'total': 15, 'repo_name': 'I4330', 'author': 'DrkSephy'}, {'total': 31, 'repo_name': 'integrated-chinese', 'author': 'DrkSephy'}, {'total': 1, 'repo_name': 'jsrecipes', 'author': 'DrkSephy'}, {'total': 20, 'repo_name': 'learn-angularJS', 'author': 'DrkSephy'}, {'total': 13, 'repo_name': 'legionJS', 'author': 'DrkSephy'}, {'total': 26, 'repo_name': 'lehman-hackathon', 'author': 'DrkSephy'}, {'total': 55, 'repo_name': 'mean-sandbox', 'author': 'DrkSephy'}, {'total': 4, 'repo_name': 'mean-stack-talk', 'author': 'DrkSephy'}, {'total': 297, 'repo_name': 'NOAA-Projects', 'author': 'DrkSephy'}, {'total': 39, 'repo_name': 'nodeapps', 'author': 'DrkSephy'}, {'total': 488, 'repo_name': 'pascal-compiler', 'author': 'DrkSephy'}, {'total': 117, 'repo_name': 'pascal-js', 'author': 'DrkSephy'}, {'total': 12, 'repo_name': 'Project-Euler', 'author': 'DrkSephy'}, {'total': 139, 'repo_name': 'python-imp-interpreter', 'author': 'DrkSephy'}, {'total': 2, 'repo_name': 'rst2pdf', 'author': 'DrkSephy'}, {'total': 2, 'repo_name': 'rust-by-example', 'author': 'DrkSephy'}, {'total': 34, 'repo_name': 'rust-sandbox', 'author': 'DrkSephy'}, {'total': 2, 'repo_name': 'satellizer', 'author': 'DrkSephy'}, {'total': 45, 'repo_name': 'smw-asm', 'author': 'DrkSephy'}, {'total': 291, 'repo_name': 'swift-sandbox', 'author': 'DrkSephy'}, {'total': 101, 'repo_name': 'Tales-of-Kratos', 'author': 'DrkSephy'}, {'total': 12, 'repo_name': 'theano-sandbox', 'author': 'DrkSephy'}, {'total': 13, 'repo_name': 'todo', 'author': 'DrkSephy'}, {'total': 18, 'repo_name': 'TV-Show-Premieres', 'author': 'DrkSephy'}, {'total': 34, 'repo_name': 'tv-show-tracker', 'author': 'DrkSephy'}, {'total': 1, 'repo_name': 'vitanao', 'author': 'DrkSephy'}, {'total': 475, 'repo_name': 'WaterEmblem', 'author': 'DrkSephy'}, {'total': 3, 'repo_name': 'webauth-ssh-authentication', 'author': 'DrkSephy'}, {'total': 3, 'repo_name': 'WebRing', 'author': 'DrkSephy'}, {'total': 15, 'repo_name': 'yabe', 'author': 'DrkSephy'}]
		with patch('hackathon.scripts.github.filterCommits') as mock_filterCommits:
			mock_filterCommits.return_value = [{'total': 488, 'repo_name': 'pascal-compiler', 'author': 'DrkSephy'}, {'total': 475, 'repo_name': 'WaterEmblem', 'author': 'DrkSephy'}, {'total': 433, 'repo_name': 'drksephy.github.io', 'author': 'DrkSephy'}, {'total': 297, 'repo_name': 'NOAA-Projects', 'author': 'DrkSephy'}, {'total': 291, 'repo_name': 'swift-sandbox', 'author': 'DrkSephy'}, {'total': 160, 'repo_name': 'git-technetium', 'author': 'DrkSephy'}, {'total': 139, 'repo_name': 'python-imp-interpreter', 'author': 'DrkSephy'}, {'total': 117, 'repo_name': 'pascal-js', 'author': 'DrkSephy'}, {'total': 101, 'repo_name': 'Tales-of-Kratos', 'author': 'DrkSephy'}]
			maxCommits = [{'total': 488, 'repo_name': 'pascal-compiler', 'author': 'DrkSephy'}, {'total': 475, 'repo_name': 'WaterEmblem', 'author': 'DrkSephy'}, {'total': 433, 'repo_name': 'drksephy.github.io', 'author': 'DrkSephy'}, {'total': 297, 'repo_name': 'NOAA-Projects', 'author': 'DrkSephy'}, {'total': 291, 'repo_name': 'swift-sandbox', 'author': 'DrkSephy'}, {'total': 160, 'repo_name': 'git-technetium', 'author': 'DrkSephy'}, {'total': 139, 'repo_name': 'python-imp-interpreter', 'author': 'DrkSephy'}, {'total': 117, 'repo_name': 'pascal-js', 'author': 'DrkSephy'}, {'total': 101, 'repo_name': 'Tales-of-Kratos', 'author': 'DrkSephy'}]
			self.assertEqual(maxCommits, maxCommits)



