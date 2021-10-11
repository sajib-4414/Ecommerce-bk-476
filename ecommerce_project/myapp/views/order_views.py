from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Order, OrderLine
from ecommerce_project.myapp.serializers.order_serializers import OrderOutputSerializer, OrderInputSerializer, \
    OrderLineOutputSerializer, OrderLineInputSerializer, OrderUpdateSerializer


class OrderListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        order_list = Order.objects.all()
        serializer = OrderOutputSerializer(order_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_order = serializer.save()
            output_serializer = OrderOutputSerializer(created_order)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderLineListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        orderline_list = OrderLine.objects.all()
        serializer = OrderLineOutputSerializer(orderline_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderLineInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_orderline = serializer.save()
            output_serializer = OrderLineOutputSerializer(created_orderline)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderOutputSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = get_object_or_404(Order, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = OrderUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            updated_order = serializer.save()
            output_serializer = OrderOutputSerializer(updated_order)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cartline = get_object_or_404(Order, pk=pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        cartline.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)
