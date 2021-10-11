from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Product, Review, Order, OrderLine, Cart
from ecommerce_project.myapp.serializers.product_related_seralizers import ProductOutputSerializer, \
    ProductInputSerializer, ReviewOutputSerializer, ReviewInputSerializer, OrderOutputSerializer, OrderInputSerializer, \
    OrderLineOutputSerializer, OrderLineInputSerializer, CartOutputSerializer


class ProductListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        product_list = Product.objects.all()
        serializer = ProductOutputSerializer(product_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_product = serializer.save()
            output_serializer = ProductOutputSerializer(created_product)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        review_list = Review.objects.all()
        serializer = ReviewOutputSerializer(review_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_review = serializer.save()
            print("I am here")
            output_serializer = ReviewOutputSerializer(created_review)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class CartListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        cart_list = Cart.objects.all()
        serializer = CartOutputSerializer(cart_list, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = OrderInputSerializer(data=request.data.copy())
    #     if serializer.is_valid():
    #         created_order = serializer.save()
    #         output_serializer = OrderOutputSerializer(created_order)
    #         return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)