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


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    #queryset = Team.objects.filter(user_id_username=self.request.user)
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        id = self.kwargs['pk']
        data = Team.objects.filter(id=id, users_id__username=self.request.user.username)
        if not data:
            raise PermissionDenied(detail=None, code=403)
        return data

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateList(generics.CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)
