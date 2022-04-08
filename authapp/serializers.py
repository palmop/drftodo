from rest_framework import serializers
from authapp.models import UserApp

class RegisterUserAppSerializer(serializers.ModelSerializer):
    
    # write_only True because we don't want to send password to the frontend
    # but only the frontend could send password ti api server.
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta():
        model = UserApp
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        return UserApp.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = UserApp
        fields = ('username', 'email', 'password', 'token')
        read_only_fields = ['token']