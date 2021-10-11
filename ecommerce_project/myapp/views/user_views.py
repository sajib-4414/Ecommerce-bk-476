from rest_framework import status
from rest_framework.views import APIView
from ecommerce_project.myapp.models import BuyerUser, SellerUser, Company
from rest_framework.response import Response
from ecommerce_project.myapp.serializers import BuyerOutputSerializer, SellerOutputSerializer
from ecommerce_project.myapp.serializers.UserSerializers import   \
      CompanyOutputSerializer, CompanyInputSerializer
from ecommerce_project.myapp.serializers.buyer_serializers import BuyerInputSerializer
from ecommerce_project.myapp.serializers.seller_serializers import SellerInputSerializer


class BuyersUserAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        buyers = BuyerUser.objects.all()
        serializer = BuyerOutputSerializer(buyers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BuyerInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_buyer = serializer.save()
            output_serializer = BuyerOutputSerializer(created_buyer)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class CompaniesAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanyOutputSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanyInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_company = serializer.save()
            output_serializer = CompanyOutputSerializer(created_company)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
