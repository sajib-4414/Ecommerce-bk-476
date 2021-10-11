from rest_framework import serializers
from ecommerce_project.myapp.models import Review, BuyerUser, Product
from ecommerce_project.myapp.serializers import ProductOutputSerializer
from ecommerce_project.myapp.serializers.buyer_serializers import BuyerOutputSerializer


class ReviewOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    user = BuyerOutputSerializer()
    product = ProductOutputSerializer()

    class Meta:
        model = Review
        fields = ['user', 'description','product', 'pk']

    def get_pk(self,obj):
        return obj.id


class ReviewInputSerializer(serializers.ModelSerializer):
    buyer_user_id = serializers.IntegerField(required=True)
    product_id = serializers.IntegerField(required=True)

    class Meta:
        model = Review
        fields = ['buyer_user_id', 'product_id','description']

    def create(self, validated_data):
        buyer_user_id = validated_data.pop('buyer_user_id')
        product_id = validated_data.pop('product_id')
        review = Review.objects.create(**validated_data)

        try:
            buyer_user = BuyerUser.objects.get(pk=buyer_user_id)
        except BuyerUser.DoesNotExist:
            raise serializers.ValidationError("userError: problem with the user for this review.")
        review.user = buyer_user

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("productError: problem with the product for this review")
        review.product = product

        review.save()
        return review
