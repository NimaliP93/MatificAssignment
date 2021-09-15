from django.contrib.auth.models import User, Group
from django.db.models import Sum

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Team, Player, Game, Score, UserActivityStatistics, UserActivitySummary


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'groups', 'last_login']
        read_only_fields = ('id',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'coach', 'avg_score']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'height', 'user', 'team', 'player_avg_score', 'tot_games_played']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class UserActivitySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivitySummary
        fields = '__all__'


class UserActivityStatisticsSerializer(serializers.ModelSerializer):
    login_count = serializers.SerializerMethodField()
    online_time = serializers.SerializerMethodField()

    @classmethod
    def get_online_time(self, object):
        sum_val = UserActivitySummary.objects.all().filter(user=object, time_duration__lte=60).aggregate(Sum('time_duration'))
        return sum_val['time_duration__sum']

    class Meta:
        model = UserActivityStatistics
        fields = ['username', 'last_login', 'online_time']


