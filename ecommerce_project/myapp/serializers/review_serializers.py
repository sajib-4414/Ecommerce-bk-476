from rest_framework import serializers
from ecommerce_project.myapp.models import Review, BuyerUser, Product
from ecommerce_project.myapp.serializers import ProductOutputSerializer
from ecommerce_project.myapp.serializers.buyer_serializers import BuyerOutputSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

class ReviewUpdateSerializer(serializers.Serializer):
    description = serializers.CharField(required=False,max_length=200)
    user_id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField(required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):
        if 'product_id' in validated_data:
            #wants to update product, have to check if the product is a valid one
            product_id = validated_data.pop('product_id')
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("productError: problem with the product for this review.")
            instance.product = product

        if 'user_id' in validated_data:
            #wants to update user, have to check if the user is a valid one
            user_id = validated_data.pop('user_id')
            try:
                buyer_user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise serializers.ValidationError("userError: problem with the user for this review.")
            instance.user = buyer_user

        if 'description' in validated_data:
            instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def validate(self, data):
        """
        This method can be used later to add any validation, the example here is to demonstrate one validation
        Check that the remind me date is before the before due date.
        """
        # print(data['remind_me_datetime'])
        # if 'remind_me_datetime' in data:
        #     if 'due_datetime' in data:
        #         if not (data['due_datetime'] > data['remind_me_datetime']):
        #             raise serializers.ValidationError({"remind_me_date": "Reminder date has to be before due date"})
        #     else:
        #         instance = getattr(self, 'instance', None)
        #         if not (instance.due_datetime > data['remind_me_datetime']):
        #             raise serializers.ValidationError({"remind_me_date": "Reminder date has to be before due date"})
        return data

    def get_pk(self,obj):
        return obj.id


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
            buyer_user = User.objects.get(pk=buyer_user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("userError: problem with the user for this review.")
        review.user = buyer_user

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("productError: problem with the product for this review")
        review.product = product

        review.save()
        return review
