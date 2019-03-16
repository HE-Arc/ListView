from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ Source : https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
     Recommand to use a custom, in case we want to add field in the future"""
    nickname = models.CharField(max_length=50, blank=True, unique=False)


