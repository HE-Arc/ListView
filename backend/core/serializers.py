from rest_framework import serializers

from core.models import Team, Board, List, Task
from auth0.models import CustomUser


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
    users_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)
    boards = BoardSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'users_id', 'boards')
