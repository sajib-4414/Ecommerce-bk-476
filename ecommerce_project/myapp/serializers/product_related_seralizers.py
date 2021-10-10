from rest_framework import serializers
from django.shortcuts import get_object_or_404
from ecommerce_project.myapp.models import Product, Category, Company, SellerUser, Review, BuyerUser, Order, OrderLine
from ecommerce_project.myapp.serializers.OtherSerializers import CategorySerializer
from ecommerce_project.myapp.serializers.UserSerializers import CompanyOutputSerializer, SellerOutputSerializer, \
    BuyerOutputSerializer


class ProductOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    category = CategorySerializer()
    company = CompanyOutputSerializer()
    seller = SellerOutputSerializer()

    class Meta:
        model = Product
        fields = ['name', 'price','quantity','delivery_cost','category', 'company','seller', 'pk']

    def get_pk(self,obj):
        return obj.id


class ProductInputSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(required=True)
    company_id = serializers.IntegerField(required=True)
    seller_id = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ['name', 'price','quantity','delivery_cost','category_id', 'company_id','seller_id']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        company_id = validated_data.pop('company_id')
        seller_id = validated_data.pop('seller_id')
        product = Product.objects.create(**validated_data)

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError("categoryError: Invalid product category")
        product.category = category

        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise serializers.ValidationError("companyError: Invalid Company chosen for the product")
        product.company = company

        try:
            seller = SellerUser.objects.get(pk=seller_id)
        except SellerUser.DoesNotExist:
            raise serializers.ValidationError("sellerError: Invalid Seller chosen for the product")
        product.seller = seller

        product.save()
        return product


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


class OrderOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    buyer = BuyerOutputSerializer()

    class Meta:
        model = Order
        fields = ['buyer', 'date','value', 'pk']

    def get_pk(self,obj):
        return obj.id


class OrderInputSerializer(serializers.ModelSerializer):
    buyer_user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Order
        fields = ['buyer_user_id', 'value']

    def create(self, validated_data):
        buyer_user_id = validated_data.pop('buyer_user_id')
        order = Order.objects.create(**validated_data)

        try:
            buyer_user = BuyerUser.objects.get(pk=buyer_user_id)
        except BuyerUser.DoesNotExist:
            raise serializers.ValidationError("userError: problem with the user for this order.")
        order.buyer = buyer_user

        order.save()
        return order


class OrderLineOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    product = ProductOutputSerializer()
    order = OrderOutputSerializer()

    class Meta:
        model = OrderLine
        fields = ['product', 'quantity', 'order', 'pk']

    def get_pk(self,obj):
        return obj.id