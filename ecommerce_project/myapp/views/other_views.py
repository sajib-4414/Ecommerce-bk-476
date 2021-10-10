from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Address
from ecommerce_project.myapp.serializers.OtherSerializers import AddressSerializer


class AddressListNCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        # logged_in_username = get_logged_in_username(request)
        address_list = Address.objects.all() #.filter(author__username=logged_in_username)
        serializer = AddressSerializer(address_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data.copy())
        # logged_in_username = get_logged_in_username(request)
        # serializer.context["username"] = logged_in_username
        if serializer.is_valid():
            created_address = serializer.save()
            output_serializer = AddressSerializer(created_address)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)