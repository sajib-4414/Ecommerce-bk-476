import json

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ecommerce_project.myapp.serializers.authentication_serializers import LoginSerializer


class GetAuthToken(APIView):
    '''
    just a manual workaround for a login
    '''
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_buyer = serializer.save()
            # newdict = {'token': "test"}
            # newdict.update(created_buyer)
            # token = created_buyer['token']
            # user = created_buyer['buyer']
            # user['token'] = token.key
            # print(type(created_buyer))
            # print(created_buyer)
            # json_string = json.dumps(created_buyer)
            return JsonResponse(created_buyer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)