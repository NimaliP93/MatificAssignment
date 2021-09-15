import base64

from django.contrib.auth.models import User, Group
from rest_framework import status

from .test_setup import TestApiSetup


class TestGameAPIViews(TestApiSetup):
    def setUp(self):
        new_group, created = Group.objects.get_or_create(name='Admin')

        self.username = 'admin'
        self.password = '123'
        self.admin_user = User.objects.create_user(username=self.username, password=self.password, is_staff=True)
        self.admin_user.groups.add(new_group)

        credentials = base64.b64encode(b'admin:123').decode("ascii")

        self.client.credentials(HTTP_AUTHORIZATION='Basic ' + credentials)

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_view_users_by_admin(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_group_by_admin(self):
        response = self.client.get(self.group_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_players_by_admin(self):
        response = self.client.get(self.player_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_team_by_admin(self):
        response = self.client.get(self.team_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_score_by_admin(self):
        response = self.client.get(self.score_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_game_by_admin(self):
        response = self.client.get(self.game_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_user_by_admin(self):
        user = {'username': 'player12',
                'password': '123',
                'email': 'player12@gmail.com'
                }

        response = self.client.post(self.user_url, user, format("json"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'player12')

    def test_post_user_with_missing_param_by_admin(self):
        user = {'username': 'player13',
                'password': '123'
                }

        response = self.client.post(self.user_url, user, format("json"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
