from rest_framework import serializers, permissions
from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUserModel
        id = model.pk

        fields = ['id', 'username', 'email']

    def create(self, validated_data):

        user = CustomUserModel(**validated_data)

        user.save()

        return user