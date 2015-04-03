import unittest
from mock import Mock, patch, MagicMock
from django.conf import settings
from hackathon.scripts.github import getUserData, getUserRepositories, getForkedRepositories


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

		# Construct the URL
		self.url = self.API_BASE_URL +  '?' + clientID + '&' + clientSecret

		# Instantiate data collection objects
		jsonList = []
		parsedData = []
		userData = {}

		with patch('hackathon.scripts.github.getUserData') as mock_getUserData:
			# Mock the return value of this method
			mock_getUserData.return_value = {'public_repos': 50, 'public_gists': 5, 'name': 'David Leonard', 'blog': 'http://drksephy.github.io', 'avatar_url': 'https://avatars.githubusercontent.com/u/1226900?v=3', 'followers': 52, 'following': 7, 'email': 'DrkSephy1025@gmail.com'}
			jsonList.append(mock_getUserData.return_value)
			for data in jsonList:
				userData['name'] = mock_getUserData.return_value['name']
				userData['blog'] = mock_getUserData.return_value['blog']
				userData['email'] = mock_getUserData.return_value['email']
				userData['public_gists'] = mock_getUserData.return_value['public_gists']
				userData['public_repos'] = mock_getUserData.return_value['public_repos']
				userData['avatar_url'] = mock_getUserData.return_value['avatar_url']
				userData['followers'] = mock_getUserData.return_value['followers']
				userData['following'] = mock_getUserData.return_value['following']
			parsedData.append(userData)
			self.assertEqual(getUserData(clientID, clientSecret), parsedData)

	def testGetUserRepositories(self):
		'''Test for github.py getUserRepositories'''

		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret

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


		repositories = ['ACM-Game-Presentation', 'ACM-Portfolio-Presentation', 'angular-nhl', 'async', 'd3-sandbox', 'Deep-Learning', 'Django-Hackathon-Starter', 
						'drksephy.github.io', 'el-gamal-attack', 'FizzBuzz-Test-1', 'flux-reactJS', 'fractals', 'git-api', 'git-technetium', 'hackathon-starter',
						'hackcity', 'hackcity.github.io', 'historicalWeather', 'I4330', 'integrated-chinese', 'jsrecipes', 'learn-angularJS', 'legionJS', 'lehman-hackathon', 
						'mean-sandbox', 'mean-stack-talk', 'NOAA-Projects', 'node', 'nodeapps', 'pascal-compiler', 'pascal-js', 'Project-Euler', 'python-imp-interpreter', 
						'rst2pdf', 'rust-by-example', 'rust-sandbox', 'satellizer', 'smw-asm', 'swift-sandbox', 'Tales-of-Kratos', 'theano-sandbox', 'todo', 'TV-Show-Premieres', 
						'tv-show-tracker', 'vitanao', 'WaterEmblem', 'webauth-ssh-authentication', 'webauth-via-ssh', 'WebRing', 'yabe']

		self.assertEqual(getUserRepositories(clientID, clientSecret), repositories)


	def testGetForkedRepositories(self):
		'''Test for github.py getForkedRepositories'''

		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		
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
		self.assertEqual(getForkedRepositories(clientID, clientSecret), forkedRepositories)



