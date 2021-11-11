import uuid

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Cart, CartLine, Product
from ecommerce_project.myapp.serializers import CartOutputSerializer, \
    CartInputSerializer, CartLineOutputSerializer, CartLineInputSerializer, CartUpdateSerializer, \
    CartLineUpdateSerializer, CartWithLinesOutputSerializer, AddToCartSerializer


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
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            raise Http404
        serializer = CartWithLinesOutputSerializer(cart)
        return Response(serializer.data)


class AddToCartUserAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''

    '''
    # def get(self, request, format=None):
    #     cartline_list = CartLine.objects.all()
    #     serializer = CartLineOutputSerializer(cartline_list, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddToCartSerializer(data=request.data.copy())
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_id = serializer.validated_data.get('user_id')
        product_id = serializer.validated_data.get('product_id')

        # now find the cart of this user, if no cart, create a cart
        try:
            user_cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            #we will create a cart for him
            unique_id = uuid.uuid4().hex[:6].upper()
            user_cart = Cart.objects.create(user_id=user_id, unique_id=unique_id)

        cart_line = None
        if Product.objects.filter(pk=product_id).exists():

            # now create a cartline for him or get existing one
            cart_line, created = CartLine.objects.get_or_create(product_id=product_id, cart_id=user_cart.id)
        else:
            raise Http404


        #coming here means cart exists, we will check if the cartline exists, if not create
        #one, if yes , just raise the quantity
        #let's find if there is any cartline exists

        if not created:
            # cartline = CartLine.objects.get(cart_id=user_cart.id, product_id=product_id)
            #cartline exists, so increase the quantity
            cart_line.quantity = (cart_line.quantity+1)
            cart_line.save()

        # except CartLine.DoesNotExist:
        #
        #     #coming here means the cartline does not exist
        #     cart_line = CartLine.objects.create(product_id=product_id, cart_id=user_cart.id, quantity=1)

        # get the cart with cartlines object from the serializer
        serializer = CartWithLinesOutputSerializer(user_cart)
        # return the cart with carlines response
        return Response(serializer.data)
