from django.test import TestCase
from django.test import Client


# cannot access teams if not logged in
class TestUnlogged(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.get('/api/teams/')

        self.assertEqual(response.status_code, 401)# unauthorized error
