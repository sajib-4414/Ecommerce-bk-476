from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce_project.myapp.models import BuyerUser
from ecommerce_project.myapp.serializers import BuyerOutputSerializer
from ecommerce_project.myapp.serializers.buyer_serializers import BuyerInputSerializer


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