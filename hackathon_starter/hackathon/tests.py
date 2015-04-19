from django.test import TestCase

# Create your tests here.

class HackathonViewsTestCase(TestCase):
	def testIndex(self):
		resp = self.client.get('/hackathon/api/')
		self.assertEqual(resp.status_code, 200)

	def testSteam(self):
		resp = self.client.get('/hackathon/steam')
		self.assertEqual(resp.status_code, 301)

	def testSteamDiscountedGames(self):
		resp = self.client.get('/hackathon/steamDiscountedGames/')
		self.assertEqual(resp.status_code, 200)

	def testQuandlDowJones(self):
		resp = self.client.get('/hackathon/quandlDowJones/')
		self.assertEqual(resp.status_code, 200)

	def testQuandlSnp500(self):
		resp = self.client.get('/hackathon/quandlSnp500/')
		self.assertEqual(resp.status_code, 200)

	def testQuandlNasdaq(self):
		resp = self.client.get('/hackathon/quandlNasdaq/')
		self.assertEqual(resp.status_code, 200)

	def testGithubUser(self):
		resp = self.client.get('/hackathon/githubUser/')
		self.assertEqual(resp.status_code, 200)