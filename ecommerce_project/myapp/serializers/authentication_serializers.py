from django.http import Http404
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from ecommerce_project.myapp.serializers import BuyerOutputSerializer

User = get_user_model()


class RequirableBooleanField(serializers.BooleanField):
    default_empty_html = serializers.empty


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=20)
    user = BuyerOutputSerializer(read_only=True)
    is_buyer = RequirableBooleanField(required=True)

    def create(self, validated_data):
        user_email = validated_data.pop('email')
        password = validated_data.pop('password')
        is_requested_user_buyer = validated_data.pop('is_buyer')
        try:
            user = User.objects.get(email=user_email,password=password)
            if is_requested_user_buyer:
                #check if we got buyer user
                if not (user.is_staff and not user.is_admin):
                    raise Http404
            else:
                #check if we got seller user, as a seller user is requested
                if not (user.is_admin and not user.is_staff):
                    raise Http404
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


