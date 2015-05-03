import unittest
from mock import Mock, patch, MagicMock
from hackathon.scripts.instagram import InstagramOauthClient, searchForLocation


class TwitterTests(unittest.TestCase):

	def setUp(self):
		self.authorization_url = 'https://api.instagram.com/oauth/authorize/?client_id='
		self.access_token_url = 'https://api.instagram.com/oauth/access_token'
		self.client_id = '77dc10b9e3624e908ce437c0a82da92e'
		self.client_secret = '8bcf3139857149aaba7acaa61288427f'
		self.googlemap_api_key = 'AIzaSyA7tttML91EGZ32S_FOOoxu-mbxN9Ojds8'


	def test_TwitterOauthClient(self):
		with patch('hackathon.scripts.instagram.requests') as mock_requests:
			mock_requests.get.return_value = mock_response = Mock()
			mock_response.status_code = 200
			mock_response.json.return_value = jsonlist = {'access_token': '32833691.77dc10b.fe8fefd1dbf44cdea759714e9fcb44f3', 'user': {'username': 'mk200789', 'bio': '', 'website': '', 'profile_picture': 'https://instagramimages-a.akamaihd.net/profiles/profile_32833691_75sq_1333679391.jpg', 'full_name': '', 'id': '32833691'}}

	def test_searchForLocation(self):
		with patch('hackathon.scripts.instagram.searchForLocation') as mock_searchForLocation:
			mock_searchForLocation.return_value = {'lat': 40.621372, 'lng': -74.00232690000001}
			result = searchForLocation('7011 14th avenue, brooklyn, ny')
			self.assertEqual(mock_searchForLocation.return_value, result)


