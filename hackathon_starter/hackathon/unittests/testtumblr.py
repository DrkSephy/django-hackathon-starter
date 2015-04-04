import unittest
from mock import Mock, patch, MagicMock
from hackathon.scripts.tumblr import getBlogInfo
import time

class TumblrTests(unittest.TestCase):
	def setUp(self):
		self.blog_uri 			= 'http://api.tumblr.com/v2/blog/'
		self.consumer_key 		= 'KrSbAc9cYLmIgVAn1D21FjRR97QWsutNMxkPDFBxo8CMWtMk4M'
		self.consumer_secret 	= 'lKWMtL2Lj8zr5pY51PVqT8ugeoG0DjrdgoFewM0QTSyJ12jP8d'
		self.user				= 'twitterthecomic'

	def testGetBlogInfo(self):
		'''Test for tumblr.py getBlogInfo method '''
		consumer_key = self.consumer_key
		consumer_secret = self.consumer_secret
		user = self.user

		# Construct url for blog info
		self.blog_info = self.blog_uri + user + ".tumblr.com/info?api_key="+ consumer_key

		with patch('hackathon.scripts.tumblr.getBlogInfo') as mock_getBlogInfo:
			# Mock the return value of this method
			mock_getBlogInfo.return_value = {'meta': {'status': 200, 'msg': 'OK'}, 
			'response': {'blog': {'ask_anon': False, 'submission_page_title': 'Submit A Tweet', 
			'updated': 1413846741, 'description': 'Comics based on the greatest tweets of our generation. \nOrganized by <a href="https://twitter.com/VectorBelly">@VectorBelly</a>.', 
			'title': 'Twitter: The Comic', 'url': 'http://twitterthecomic.tumblr.com/', 'ask_page_title': 'Submit A Tweet', 
			'share_likes': False, 'posts': 146, 'is_nsfw': False, 'ask': False, 'name': 'twitterthecomic'}}}
			jsonlist = mock_getBlogInfo.return_value
			self.meta = jsonlist['meta']
			self.response = jsonlist['response']
			self.blog = self.response['blog']
			self.blog['blog'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.blog['updated']))
			self.assertEqual(getBlogInfo(user),self.blog)
