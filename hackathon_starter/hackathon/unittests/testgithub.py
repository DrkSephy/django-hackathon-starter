import unittest
from mock import Mock, patch, MagicMock
from django.conf import settings
import hackathon.scripts.github as github

class GithubTests(unittest.TestCase):

	def setUp(self):
		self.API_BASE_URL = 'https://api.github.com/users/DrkSephy'
		self.clientID = 'client_id=2404a1e21aebd902f6db'
		self.clientSecret = 'client_secret=3da44769d4b7c9465fa4c812669148a163607c23'
		self.jsonList = []
		
	@patch.object(github, 'getUserData')
	def testGetUserData(self, mock_getUserData):
		self.url = self.API_BASE_URL +  '?' + self.clientID + '&' + self.clientSecret
		userData = Mock()
		match = {'name': 'test', 'blog': 'test', 'email': 'test', 'public_gists': 'test', 'public_repos': 'test','avatar_url': 'test', 'followers': 'test','following': 'test'}
		mock_getUserData.return_value = {'name': 'test', 'blog': 'test', 'email': 'test', 'public_gists': 'test', 'public_repos': 'test','avatar_url': 'test', 'followers': 'test','following': 'test'}
		self.assertEqual(github.getUserData(self.clientID, self.clientSecret), {'name': 'test', 'blog': 'test', 'email': 'test', 'public_gists': 'test', 'public_repos': 'test','avatar_url': 'test', 'followers': 'test','following': 'test'})

		# self.assertEqual('hello', 'hello')
