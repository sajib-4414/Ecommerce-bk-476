from django.http import Http404
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from ecommerce_project.myapp.serializers import BuyerOutputSerializer

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=20)
    user = BuyerOutputSerializer()

    def create(self, validated_data):
        user_email = validated_data.pop('email')
        password = validated_data.pop('password')
        try:
            user = User.objects.get(email=user_email,password=password)
        except User.DoesNotExist:
            raise Http404
        token, created = Token.objects.get_or_create(user=user)
        return { 'token': token}

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=20)
    user = BuyerOutputSerializer(read_only=True)

    def create(self, validated_data):
        user_email = validated_data.pop('email')
        password = validated_data.pop('password')
        try:
            user = User.objects.get(email=user_email,password=password)
        except User.DoesNotExist:
            raise Http404
        token, created = Token.objects.get_or_create(user=user)
        buyer = BuyerOutputSerializer(user)
        newdict = {'token': token.key}
        if user.staff and not user.admin:
            newdict.update({"buyer":buyer.data})
        else:
            newdict.update({"seller": buyer.data})
        return newdict

