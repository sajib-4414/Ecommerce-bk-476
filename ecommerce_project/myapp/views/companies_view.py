from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Company
from rest_framework.response import Response
from ecommerce_project.myapp.serializers.company_serializers import \
    CompanyOutputSerializer, CompanyInputSerializer, CompanyUpdateSerializer


def get_company_object(pk):
    try:
        return Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        raise Http404

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

class CompaniesDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        company = get_company_object(pk)
        serializer = CompanyOutputSerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = get_company_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = CompanyUpdateSerializer(company, data=request.data)
        if serializer.is_valid():
            updated_company = serializer.save()
            output_serializer = CompanyOutputSerializer(updated_company)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cartline = get_company_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        cartline.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)
