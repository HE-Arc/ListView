from rest_framework import serializers

from core.models import Team, Board, List, Task
from auth0.models import CustomUser


class TaskSerializer(serializers.ModelSerializer):
    belongs_to = serializers.PrimaryKeyRelatedField(queryset=List.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'checked', 'description', 'belongs_to')


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    belongs_to = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = List
        fields = ('id', 'name', 'tasks', 'belongs_to')


class BoardDetailSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'lists')


class BoardSerializer(serializers.ModelSerializer):
    belongs_to = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Board
        fields = ('id', 'name', 'belongs_to')


class TeamSerializer(serializers.ModelSerializer):
    part_of = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)
    boards = BoardSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'part_of', 'boards')
