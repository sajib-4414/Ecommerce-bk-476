from rest_framework import status
from rest_framework.views import APIView
from ecommerce_project.myapp.models import SellerUser, Company
from rest_framework.response import Response
from ecommerce_project.myapp.serializers.company_serializers import   \
      CompanyOutputSerializer, CompanyInputSerializer


class CompaniesAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    '''
    only for list and creation
    '''
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanyOutputSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanyInputSerializer(data=request.data.copy())
        if serializer.is_valid():
            created_company = serializer.save()
            output_serializer = CompanyOutputSerializer(created_company)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
