from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Product
from ecommerce_project.myapp.serializers.product_related_seralizers import ProductOutputSerializer, \
    ProductInputSerializer


def get_product_object(pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404


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


class ProductDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        """
        anyone should be able to view any post
        """
        product = get_product_object(pk)
        serializer = ProductOutputSerializer(product)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     """
    #     only author should be able to update his post
    #     """
    #     post = get_product_object(pk)
    #     validate_if_post_or_comment_owner_logged_in(request, post)
    #     serializer = PostUpdateSerializer(post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     """
    #     only author should be able to delete his post
    #     """
    #     post = get_product_object(pk)
    #     validate_if_post_or_comment_owner_logged_in(request, post)
    #     post.delete()
    #     return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)