from django.test import TestCase

# Create your tests here.

class HackathonViewsTestCase(TestCase):
	def testIndex(self):
		resp = self.client.get('/hackathon/api/')
		self.assertEqual(resp.status_code, 200)