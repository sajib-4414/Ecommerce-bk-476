from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import SellerUser
from ecommerce_project.myapp.serializers import SellerOutputSerializer
from ecommerce_project.myapp.serializers.seller_serializers import SellerInputSerializer


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