from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.permissions import IsAdminUser

import base64


class TestApiSetup(APITestCase):
    user_url = 'http://127.0.0.1:8000/user/'
    group_url = 'http://127.0.0.1:8000/group/'
    team_url = 'http://127.0.0.1:8000/team/'
    player_url = 'http://127.0.0.1:8000/player/'
    game_url = 'http://127.0.0.1:8000/game/'
    score_url = 'http://127.0.0.1:8000/score/'

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="123")
        credentials = base64.b64encode(b'testuser:123').decode("ascii")
        self.client.credentials(HTTP_AUTHORIZATION='Basic ' + credentials)

        return super().setUp()

    def tearDown(self):
        return super().tearDown()