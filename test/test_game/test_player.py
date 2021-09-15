from rest_framework import status

from .test_setup import TestApiSetup


class TestPlayerGameAPIViews(TestApiSetup):

    def test_view_users_by_player(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_group_by_player(self):
        response = self.client.get(self.group_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_players_by_player(self):
        response = self.client.get(self.player_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_team_by_player(self):
        response = self.client.get(self.team_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_score_by_player(self):
        response = self.client.get(self.score_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_game_by_player(self):
        response = self.client.get(self.game_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_user_by_player(self):
        user = {'username': 'player12',
                'password': '123',
                'email': 'player12@gmail.com'
                }

        response = self.client.post(self.user_url, user, format("json"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

