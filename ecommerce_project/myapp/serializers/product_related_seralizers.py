from rest_framework import serializers
from django.shortcuts import get_object_or_404
from ecommerce_project.myapp.models import Product, Category, Company, SellerUser
from ecommerce_project.myapp.serializers.OtherSerializers import CategorySerializer
from ecommerce_project.myapp.serializers.UserSerializers import CompanyOutputSerializer, SellerOutputSerializer
from django.core.exceptions import ObjectDoesNotExist

class ProductOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    category = CategorySerializer()
    company = CompanyOutputSerializer()
    seller = SellerOutputSerializer()
    # address = AddressSerializer()

    class Meta:
        model = Product
        fields = ['name', 'price','quantity','delivery_cost','category', 'company','seller', 'pk']

    def get_pk(self,obj):
        return obj.id


class ProductInputSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # company = CompanyOutputSerializer()
    # seller = SellerOutputSerializer()
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
