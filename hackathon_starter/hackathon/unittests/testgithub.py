import unittest
from mock import Mock, patch, MagicMock
from django.conf import settings
from hackathon.scripts.github import getUserData 


class GithubTests(unittest.TestCase):

	def setUp(self):
		self.API_BASE_URL = 'https://api.github.com/users/DrkSephy'
		self.clientID = 'client_id=2404a1e21aebd902f6db'
		self.clientSecret = 'client_secret=3da44769d4b7c9465fa4c812669148a163607c23'
	#@patch.object(github, 'getUserData')
	def testGetUserData(self):
		# Client and Secret ID
		clientID = self.clientID
		clientSecret = self.clientSecret
		# Construct the URL
		
		self.url = self.API_BASE_URL +  '?' + clientID + '&' + clientSecret
		jsonList = []
		parsedData = []
		userData = {}
		with patch('hackathon.scripts.github.getUserData') as mock_getUserData:
			print 'hello'
			# match = {'name': 'test', 'blog': 'test', 'email': 'test', 'public_gists': 'test', 'public_repos': 'test','avatar_url': 'test', 'followers': 'test','following': 'test'}
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
			print parsedData
			self.assertEqual(getUserData(clientID, clientSecret), parsedData)
