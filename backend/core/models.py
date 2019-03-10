from django.db import models
from auth0.models import CustomUser


class Team(models.Model):
    name = models.CharField(max_length=100)
    part_of = models.ManyToManyField(CustomUser, related_name='team', blank=True)

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=100)
    belongs_to = models.ForeignKey(Team, related_name='boards', on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=100)
    belongs_to = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=100)
    checked = models.BooleanField()
    description = models.CharField(max_length=500)
    belongs_to = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE)
