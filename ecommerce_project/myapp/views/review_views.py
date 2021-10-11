from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce_project.myapp.models import Review
from ecommerce_project.myapp.serializers import ReviewOutputSerializer, ReviewInputSerializer


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