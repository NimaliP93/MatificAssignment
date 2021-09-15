from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .permissions import IsAdmin, IsAdminOrCoach, is_user_in_group
from .services import get_players_with_percentile
from .models import Team, Player, Game, Score
from .serializers import TeamSerializer, PlayerSerializer, GameSerializer, ScoreSerializer, UserSerializer, \
    GroupSerializer, UserActivityStatisticsSerializer


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrCoach]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get_queryset(self):
        queryset = Player.objects.all()
        team_id = self.request.query_params.get('team_id')
        percentile = self.request.query_params.get('percentile')
        if team_id is not None:
            queryset = Player.objects.filter(team=team_id)

        if percentile is not None:
            if is_user_in_group(self.request.user.id, 'Coach'):
                queryset = queryset.filter(team__coach=self.request.user.id)
            queryset = get_players_with_percentile(queryset, percentile)
        return queryset


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class ScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class UserActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserActivityStatisticsSerializer
    http_method_names = ['get']



