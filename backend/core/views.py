from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework.exceptions import PermissionDenied

from auth0.serializers import UserSerializer
from auth0.models import CustomUser
from core.models import Team, Board, Task, List
from core.serializers import TeamSerializer, BoardSerializer, BoardDetailSerializer, TaskSerializer, ListSerializer

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = CustomUser.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(Q(username__contains=name) | Q(email__contains=name) | Q(nickname__contains=name)).distinct()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = request.user.team

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(Q(name__contains=name) | Q(boards__name__contains=name)).distinct()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        if len(data['users_id']) < 1:
            data['users_id'] = [UserSerializer(request.user).data]

        serializer = TeamSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TeamAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id = view.kwargs['pk']
        team = Team.objects.filter(id=id, users_id__username=request.user.username).exists()
        return team

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,TeamAccessPermission,)

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

class BoardAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id = view.kwargs['pk']
        board = Board.objects.filter(id=id, team_id__users_id__username=request.user.username).exists()
        return board

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    permission_classes = (permissions.IsAuthenticated,BoardAccessPermission,)


class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TaskAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id = view.kwargs['pk']
        task = Task.objects.filter(id=id, list_id__board_id__team_id__users_id__username=request.user.username).exists()
        return task

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,TaskAccessPermission)


class CreateList(generics.CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ListAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id = view.kwargs['pk']
        list = List.objects.filter(id=id, board_id__team_id__users_id__username=request.user.username).exists()
        return list

class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,ListAccessPermission,)
