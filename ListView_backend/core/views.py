from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from core.models import Team, CustomUser
from core.serializers import TeamSerializer, UserSerializer


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


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser
    serializer_class = UserSerializer
