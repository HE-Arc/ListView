from django.test import TestCase
from django.test import Client

from auth0.models import CustomUser
from core.models import Team

# cannot access teams if not logged in
class TestUnlogged(TestCase):
    def setUp(self):
        self.client = Client()

    def test_unlogged(self):
        response = self.client.get('/api/teams/')

        self.assertEqual(response.status_code, 401)# unauthorized error

# can access teams if logged in
class TestLogIn(TestCase):
    def setUp(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])

    def test_logged(self):
        response = self.client.get('/api/teams/')

        self.assertEqual(response.status_code, 200)

# create a team with testuser as a part of it, checks if testuser has access to it's detail
class TestTeamDetailAvailable(TestCase):
    def setUp(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])

        team = Team.objects.create(id=1, name='test')
        team.users_id.set([CustomUser.objects.get(username='testuser')])
        team.save()

    def test_logged(self):
        response = self.client.get('/api/teams/1/')

        self.assertEqual(response.status_code, 200)

# create a team without testuser as a part of it, checks if testuser doesn't have access to it's detail
class TestTeamDetailUnavailable(TestCase):
    def setUp(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='testuser')[0])

        team = Team.objects.create(id=1, name='test')
        team.save()

    def test_logged(self):
        response = self.client.get('/api/teams/1/')

        self.assertEqual(response.status_code, 403)


