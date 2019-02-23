from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Team, CustomUser


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'team')
