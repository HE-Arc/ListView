from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    """ Source : https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
     Recommand to use a custom, in case we want to add field in the future"""
    pass


class Team(models.Model):
    name = models.CharField(max_length=100)
    part_of = models.ManyToManyField(CustomUser, related_name='team', blank=True)

    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Team, related_name='boards', on_delete=models.CASCADE)
