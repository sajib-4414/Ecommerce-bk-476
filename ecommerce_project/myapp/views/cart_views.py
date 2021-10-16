from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Cart, CartLine
from ecommerce_project.myapp.serializers import CartOutputSerializer, \
    CartInputSerializer, CartLineOutputSerializer, CartLineInputSerializer, CartUpdateSerializer, \
    CartLineUpdateSerializer, CartWithLinesOutputSerializer


def get_cart_object(pk):
    try:
        return Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        raise Http404

def get_cartline_object(pk):
    try:
        return CartLine.objects.get(pk=pk)
    except CartLine.DoesNotExist:
        raise Http404


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

class CartDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        cart = get_cart_object(pk)
        serializer = CartOutputSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart = get_cart_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = CartUpdateSerializer(cart, data=request.data)
        if serializer.is_valid():
            updated_cart = serializer.save()
            output_serializer = CartOutputSerializer(updated_cart)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = get_cart_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        review.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)


class CartLineDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        cartline = get_cartline_object(pk)
        serializer = CartLineOutputSerializer(cartline)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cartline = get_cartline_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = CartLineUpdateSerializer(cartline, data=request.data)
        if serializer.is_valid():
            updated_cartline = serializer.save()
            output_serializer = CartLineOutputSerializer(updated_cartline)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cartline = get_cartline_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        cartline.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)


class CartlWithCartLinesForUserAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, user_id, format=None):
        cart = Cart.objects.get(user_id=user_id)
        serializer = CartWithLinesOutputSerializer(cart)
        return Response(serializer.data)