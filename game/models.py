from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Q, Avg


class Team(models.Model):
    name = models.CharField('name', unique=True, max_length=150)
    coach = models.ForeignKey(User, related_name='coach', on_delete=models.CASCADE)

    @property
    def avg_score(self):
        score = Score.objects.filter(player__team=self.id).aggregate(Sum('score'))
        total_score = score['score__sum']
        no_of_games_played = len(Game.objects.filter(Q(team1=self.id) | Q(team2=self.id)))

        if no_of_games_played == 0 or total_score is None:
            return 0

        return float(total_score) / no_of_games_played

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField('name', max_length=150)
    height = models.IntegerField(help_text='height in cm')
    user = models.ForeignKey(User, related_name='player', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE)

    @property
    def player_avg_score(self):
        score = Score.objects.filter(player__id=self.id).aggregate(Avg('score'))
        avg_score = score['score__avg']

        if avg_score is None:
            return 0
        else:
            return avg_score

    @property
    def tot_games_played(self):
        return Score.objects.filter(player__id=self.id).count()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField('name', max_length=150)
    avenue = models.CharField('stadium_name', max_length=150)
    date_played = models.DateField()
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='winner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(Player, related_name='player', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='game', on_delete=models.CASCADE)
    score = models.IntegerField()


class UserActivitySummary(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    time_duration = models.IntegerField('activity_time', default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=200, default='activity')


class UserActivityStatistics(models.Model):

    @property
    def username(self):
        return User.objects.get(self.id).username

    @property
    def last_login(self):
        return User.objects.get(self.id).last_login







