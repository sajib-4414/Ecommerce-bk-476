from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Product
from ecommerce_project.myapp.serializers.product_related_seralizers import ProductOutputSerializer


class ProductListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        product_list = Product.objects.all()
        serializer = ProductOutputSerializer(product_list, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = CategorySerializer(data=request.data.copy())
    #     if serializer.is_valid():
    #         created_category = serializer.save()
    #         output_serializer = CategorySerializer(created_category)
    #         return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)