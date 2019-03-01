from rest_framework import serializers
from core.models import Team, CustomUser


class TeamSerializer(serializers.ModelSerializer):
    part_of = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'part_of')


class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'team')

    def create(self, validated_data, **kwargs):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
