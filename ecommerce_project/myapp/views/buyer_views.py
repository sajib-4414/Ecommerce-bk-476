from django.http import Http404
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import BuyerUser
from ecommerce_project.myapp.serializers import BuyerOutputSerializer
from ecommerce_project.myapp.serializers.buyer_serializers import BuyerInputSerializer, BuyerUpdateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

def get_buyer_user_object(pk):
    try:
        return User.objects.get(pk=pk)
    except BuyerUser.DoesNotExist:
        raise Http404


class BuyersUserAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        buyers = User.objects.filter(staff=True,admin=False)
        serializer = BuyerOutputSerializer(buyers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BuyerInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_buyer = serializer.save()
            output_serializer = BuyerOutputSerializer(created_buyer)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        buyer = get_buyer_user_object(pk)
        serializer = BuyerOutputSerializer(buyer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        buyer = get_buyer_user_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = BuyerUpdateSerializer(buyer, data=request.data)
        if serializer.is_valid():
            updated_buyer = serializer.save()
            output_serializer = BuyerOutputSerializer(updated_buyer)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = get_buyer_user_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        product.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)