from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Cart, CartLine
from ecommerce_project.myapp.serializers import  CartOutputSerializer, \
    CartInputSerializer, CartLineOutputSerializer, CartLineInputSerializer

class CartListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        cart_list = Cart.objects.all()
        serializer = CartOutputSerializer(cart_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_order = serializer.save()
            output_serializer = CartOutputSerializer(created_order)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartLineListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        cartline_list = CartLine.objects.all()
        serializer = CartLineOutputSerializer(cartline_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartLineInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_cartline = serializer.save()
            output_serializer = CartLineOutputSerializer(created_cartline)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)