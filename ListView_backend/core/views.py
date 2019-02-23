from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import generics
from core.models import Team
from core.serializers import UserSerializer, TeamSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, team):
        team.save(owner=self.request.user)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
