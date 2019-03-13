from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from core.models import Team, Board, Task, List
from core.serializers import TeamSerializer, BoardSerializer, BoardDetailSerializer, TaskSerializer, ListSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = request.user.team
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        print(serializer)
        print("COUCO")
        serializer.save(part_of=[self.request.user])


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)


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
