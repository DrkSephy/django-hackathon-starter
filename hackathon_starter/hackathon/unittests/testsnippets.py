from hackathon.models import Snippet
from rest_framework import status
from rest_framework.test import APITestCase


class SnippetViewTestCase(APITestCase):
    def setUp(self):
        self.s1 = Snippet.objects.create(title='t1', code="""print("Hello, World.")""")
        self.s2 = Snippet.objects.create(title='t2', code="""print("Goodbye, World.")""")
        super(SnippetViewTestCase, self).setUp()

    def test_list(self):
        response = self.client.get('/hackathon/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_detail(self):
        response = self.client.get('/hackathon/snippets/{}/'.format(self.s1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.s1.id)

    def test_create(self):
        payload = {'title': 't3', 'code': """print("Create, World.")"""}
        response = self.client.post('/hackathon/snippets/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 't3')
        self.assertEqual(response.data['code'], """print("Create, World.")""")

    def test_update(self):
        payload = {'title': 't666', 'code': '2 + 2'}
        response = self.client.put('/hackathon/snippets/{}/'.format(self.s1.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 't666')
        self.assertEqual(response.data['code'], '2 + 2')

    def test_partial_update(self):
        payload = {'title': 't666'}
        response = self.client.patch('/hackathon/snippets/{}/'.format(self.s1.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 't666')

    def test_delete(self):
        response = self.client.delete('/hackathon/snippets/{}/'.format(self.s1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippet.objects.count(), 1)
