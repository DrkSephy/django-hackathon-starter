from django.test import TestCase

# Create your tests here.

class HackathonViewsTestCase(TestCase):
	def testIndex(self):
		resp = self.client.get('/hackathon/api/')
		self.assertEqual(resp.status_code, 200)

	def testSteam(self):
		resp = self.client.get('/hackathon/steam/')
		self.assertEqual(resp.status_code, 200)

	def testSteamDiscountedGames(self):
		resp = self.client.get('/hackathon/steamDiscountedGames/')
		self.assertEqual(resp.status_code, 200)

	def testSteamPlaytimeForever(self):
		resp = self.client.get('/hackathon/steam/')
		for dict in resp.context:
			if 'playtime_forever' in dict:
				self.assertTrue('playtime_forever' in dict)

	def testSteamName(self):
		resp = self.client.get('/hackathon/steam/')
		for dict in resp.context:
			if 'name' in dict:
				self.assertTrue('name' in dict)

	def testSteamImg(self):
		resp = self.client.get('/hackathon/steam/')
		for dict in resp.context:
			self.assertTrue('name' in dict)


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

	def testGithubTopRepositories(self):
		resp = self.client.get('/hackathon/githubTopRepositories/')
		self.assertEqual(resp.status_code, 200)

	def testGithubResume(self):
		resp = self.client.get('/hackathon/githubResume/')
		self.assertEqual(resp.status_code, 200)

	def testTwilio(self):
		resp = self.client.get('/hackathon/twilio/')
		self.assertEqual(resp.status_code, 200)
