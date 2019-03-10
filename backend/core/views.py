from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from core.models import Team, Board
from core.serializers import TeamSerializer, BoardSerializer, BoardDetailSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = request.user.team
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, **kwargs):
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
