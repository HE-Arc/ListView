from django.db import models
from auth0.models import CustomUser


class Team(models.Model):
    name = models.CharField(max_length=100)
    users_id = models.ManyToManyField(CustomUser, related_name='team', blank=True)

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=100)
    team_id = models.ForeignKey(Team, related_name='boards', on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=100)
    board_id = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=100)
    checked = models.BooleanField()
    description = models.CharField(max_length=500, null=True, blank=True)
    list_id = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE)
