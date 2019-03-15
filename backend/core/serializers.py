from rest_framework import serializers, exceptions

from auth0.models import CustomUser
from auth0.serializers import UserSerializer
from core.models import Team, Board, List, Task


class TaskSerializer(serializers.ModelSerializer):
    list_id = serializers.PrimaryKeyRelatedField(queryset=List.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'checked', 'description', 'list_id')


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    board_id = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = List
        fields = ('id', 'name', 'tasks', 'board_id')


class BoardDetailSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'lists')


class BoardSerializer(serializers.ModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Board
        fields = ('id', 'name', 'team_id')


class TeamSerializer(serializers.ModelSerializer):
    users_id = UserSerializer(many=True, read_only=False)
    boards = BoardSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'users_id', 'boards')

    def create(self, validated_data):
        users_data = validated_data.pop('users_id')
        team = Team.objects.create(**validated_data)
        users = []
        for user_data in users_data:
            users.append(CustomUser.objects.get(username=user_data['username']))
        team.users_id.set(users)
        return team

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        users_data = validated_data.pop('users_id')
        if len(users_data) > 0:  # Don't update if there is no more user in the team
            users = []
            for user_data in users_data:
                users.append(CustomUser.objects.get(username=user_data['username']))
            instance.users_id.set(users)
            return instance
        return exceptions.APIException

