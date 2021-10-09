from rest_framework.views import APIView
from ecommerce_project.myapp.models import BuyerUser, SellerUser
from rest_framework.response import Response

from ecommerce_project.myapp.serializers.UserSerializers import BuyerOutputSerializer, SellerOutputSerializer


class BuyersUserAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        # logged_in_username = get_logged_in_username(request)
        buyers = BuyerUser.objects.all() #.filter(author__username=logged_in_username)
        serializer = BuyerOutputSerializer(buyers, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = CommentInputSerializer(data=request.data.copy())
    #     logged_in_username = get_logged_in_username(request)
    #     serializer.context["username"] = logged_in_username
    #     if serializer.is_valid():
    #         created_comment = serializer.save()
    #         output_serializer = CommentOutputSerializer(created_comment)
    #         return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellersUserAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        # logged_in_username = get_logged_in_username(request)
        sellers = SellerUser.objects.all() #.filter(author__username=logged_in_username)
        serializer = SellerOutputSerializer(sellers, many=True)
        return Response(serializer.data)
