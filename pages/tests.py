from django.http import response
from django.test import SimpleTestCase


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_status(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
