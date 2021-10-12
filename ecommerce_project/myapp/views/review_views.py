from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecommerce_project.myapp.models import Review
from ecommerce_project.myapp.serializers import ReviewOutputSerializer, ReviewInputSerializer, ReviewUpdateSerializer


def get_review_object(pk):
    try:
        return Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        raise Http404

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


class ReviewDetailUpdateDeleteAPIView(APIView):
    """
    Retrieve, update or delete a object instance.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        review = get_review_object(pk)
        serializer = ReviewOutputSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        review = get_review_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        serializer = ReviewUpdateSerializer(review, data=request.data)
        if serializer.is_valid():
            updated_review = serializer.save()
            output_serializer = ReviewOutputSerializer(updated_review)
            return Response(output_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = get_review_object(pk)
        # validate_if_post_or_comment_owner_logged_in(request, post)
        review.delete()
        return Response({"delete": "delete success"},status=status.HTTP_204_NO_CONTENT)