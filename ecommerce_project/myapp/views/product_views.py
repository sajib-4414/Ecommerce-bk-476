from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Product
from ecommerce_project.myapp.serializers import ProductUpdateSerializer, ProductInputSerializer, ProductOutputSerializer


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
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        product = get_product_object(pk)
        serializer = ProductOutputSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = get_product_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            updated_product = serializer.save()
            output_serializer = ProductOutputSerializer(updated_product)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = get_product_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        product.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)


class ProductListByCategoryAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    '''
    def get(self, request, category_name, format=None):
        product_list = Product.objects.filter(category__name__contains=category_name)
        serializer = ProductOutputSerializer(product_list, many=True)
        return Response(serializer.data)

class ProductListBySearchKeywordsAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    '''
    def get(self, request, keywords, format=None):
        product_list = Product.objects.filter(Q(name__contains=keywords)|Q(category__name__contains=keywords)|Q(company__CompanyName__contains=keywords))
        serializer = ProductOutputSerializer(product_list, many=True)
        return Response(serializer.data)


class ProductListByCompanyAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    '''
    def get(self, request, company_id, format=None):
        product_list = Product.objects.filter(company_id=company_id)
        serializer = ProductOutputSerializer(product_list, many=True)
        return Response(serializer.data)

class ProductListBySellerAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    '''
    def get(self, request, seller_id, format=None):
        product_list = Product.objects.filter(seller_id=seller_id)
        serializer = ProductOutputSerializer(product_list, many=True)
        return Response(serializer.data)