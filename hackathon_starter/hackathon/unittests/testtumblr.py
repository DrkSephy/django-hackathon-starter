import unittest
from mock import Mock, patch, MagicMock
from hackathon.scripts.tumblr import *
import oauth2
import urlparse
from django.conf import settings

class TestTumblr(unittest.TestCase):

	def setUp(self):
		self.consumer_key = 'KrSbAc9cYLmIgVAn1D21FjRR97QWsutNMxkPDFBxo8CMWtMk4M'
		self.consumer_secret = 'lKWMtL2Lj8zr5pY51PVqT8ugeoG0DjrdgoFewM0QTSyJ12jP8d'
		self.consumer = oauth2.Consumer(key=self.consumer_key, secret=self.consumer_secret)
		self.tumblrclient = TumblrOauthClient(self.consumer_key, self.consumer_secret)#, 'QBXdeeMKAnLzDbIG7dDNewTzRYyQoHZLbcn3bAFTCEFF5EXurl')
		self.authorize = self.tumblrclient.authorize_url()

		
	def test_init(self):
		self.assertEqual(self.consumer.key, self.consumer_key)
		self.assertEqual(self.consumer.secret, self.consumer_secret)

	#def test_get_authorize_url(self):
	#	self.client = oauth2.Client(self.consumer)
	#	self.assertEqual(self.client.consumer, self.consumer)
	#	with patch('hackathon.scripts.tumblr.TumblrOauthClient.authorize_url') as mock_get_authorize_url:
	#		mock_get_authorize_url.return_value = "oauth_token=QBXdeeMKAnLzDbIG7dDNewTzRYyQoHZLbcn3bAFTCEFF5EXurl&oauth_token_secret=u10SuRl2nzS8vFK4K7UPQexAvbIFBFrZBjA79XDlgoXFxv9ZhO&oauth_callback_confirmed=true"
	#		self.request_token = dict(urlparse.parse_qsl(mock_get_authorize_url.return_value))
	#		self.oauth_token = self.request_token['oauth_token']
	#		self.oauth_token_secret = self.request_token['oauth_token_secret']		
	#		link = "http://www.tumblr.com/oauth/authorize?oauth_token="+self.oauth_token+"&redirect_uri=http%3A%2F%2Flocalhost%3A8000/hackathon/tumblr"
	#		self.assertEqual(self.authorize,link )