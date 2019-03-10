from rest_framework import serializers

from auth0.models import CustomUser
from core.serializers import TeamSerializer


class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'name', 'team')

    # def create(self, validated_data, **kwargs):
    #     user = super().create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    def update(self, instance, validated_data):
        print(validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
