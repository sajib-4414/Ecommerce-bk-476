from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import SellerUser
from ecommerce_project.myapp.serializers import SellerOutputSerializer
from ecommerce_project.myapp.serializers.seller_serializers import SellerInputSerializer, SellerUpdateSerializer


class SellersUserAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        sellers = SellerUser.objects.all()
        serializer = SellerOutputSerializer(sellers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SellerInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_seller = serializer.save()
            output_serializer = SellerOutputSerializer(created_seller)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        seller = get_object_or_404(SellerUser, pk=pk)
        serializer = SellerOutputSerializer(seller)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        seller = get_object_or_404(SellerUser, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = SellerUpdateSerializer(seller, data=request.data)
        if serializer.is_valid():
            updated_seller = serializer.save()
            output_serializer = SellerOutputSerializer(updated_seller)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        seller = get_object_or_404(SellerUser, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        seller.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)