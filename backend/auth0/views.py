import jwt
from django.http import JsonResponse
from functools import wraps
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from auth0.models import CustomUser
from auth0.serializers import UserSerializer


class UserGetId(APIView):
    def get(self, request):
        return Response(request.user.id)


class UserUpdate(generics.UpdateAPIView):
    queryset = CustomUser
    serializer_class = UserSerializer


def get_token_auth_header(request):
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]
    return token


def requires_scope(required_scope):
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            unverified_claims = jwt.get_unverified_claims(token)
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return f(*args, **kwargs)
            response = JsonResponse({'message': 'You dont have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope
