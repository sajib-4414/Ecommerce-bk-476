from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=20)

    def create(self, validated_data):
        user_email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.get(email=user_email,password=password)
        token, created = Token.objects.get_or_create(user=user)
        return { 'token': token}
