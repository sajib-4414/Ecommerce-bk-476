from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Address, Category
from ecommerce_project.myapp.serializers.other_serializers import AddressSerializer, CategorySerializer, \
    AddressUpdateSerializer, CategoryUpdateSerializer
from django.db import models


class AddressListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        address_list = Address.objects.all()
        serializer = AddressSerializer(address_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_address = serializer.save()
            output_serializer = AddressSerializer(created_address)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data.copy())
        if serializer.is_valid():
            created_category = serializer.save()
            output_serializer = CategorySerializer(created_category)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        address = get_object_or_404(Address, pk=pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address = get_object_or_404(Address, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = AddressUpdateSerializer(address, data=request.data)
        if serializer.is_valid():
            updated_address = serializer.save()
            output_serializer = AddressSerializer(updated_address)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = get_object_or_404(Address, pk=pk)
        #find if this is associated with other models
        if hasattr(address, 'address_of') or hasattr(address, 'company_address_of'):
            #means there is a buyer user with this address cannot be deleted
            # print(address.company_address_of)
            return Response({"addressError: This address cannot be deleted"}, status=status.HTTP_400_BAD_REQUEST)
        # print(address.address_of)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        address.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)


class CategoryDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = get_object_or_404(Category, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = CategoryUpdateSerializer(category, data=request.data)
        if serializer.is_valid():
            updated_category = serializer.save()
            output_serializer = CategorySerializer(updated_category)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = get_object_or_404(Category, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        category.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)