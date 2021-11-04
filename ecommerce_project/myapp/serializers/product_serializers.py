from rest_framework import serializers
from ecommerce_project.myapp.models import Category, Company, Product
from ecommerce_project.myapp.serializers.seller_serializers import SellerOutputSerializer
from ecommerce_project.myapp.serializers.other_serializers import CategorySerializer
from ecommerce_project.myapp.serializers.company_serializers import CompanyOutputSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

"""
The purpose of the serializers are to create, update, read Product Objects on/from the database
and return them to the views for the REST API response.
We use three dedicated serializers for the create, read, update operations. The reason is,
we can employ specific business logic, input pattern, and validation on the APIs.
We use the inputserializer to create a product, outputserializer to output 
the product properties in the designated format, and use the updateserializer 
to update the product properties.
"""


class ProductInputSerializer(serializers.ModelSerializer):
    """
    These id fields are declared as an extra on the serializer.Although they output
    as respective objects, they input as id
    For example, we want to input the category as a category_id, so we can pick the right
    preexisting category
    """
    category_id = serializers.IntegerField(required=True)
    company_id = serializers.IntegerField(required=True)
    seller_id = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'delivery_cost', 'category_id', 'company_id', 'seller_id']

    def create(self, validated_data):
        category_id = validated_data.get('category_id')
        company_id = validated_data.get('company_id')
        seller_id = validated_data.get('seller_id')

        # validating the foreign keys
        if not Category.objects.filter(pk=category_id).exists():
            raise serializers.ValidationError("Error: Category does not exist")
        if not Company.objects.filter(pk=company_id).exists():
            raise serializers.ValidationError("Error: Company does not exist")
        if not User.objects.filter(pk=seller_id).exists():
            raise serializers.ValidationError("Error: Seller does not exist")

        '''
        At this point, it means, all the provided foreign keys are valid, so we can
        safely create product object
        '''
        product = Product.objects.create(**validated_data)
        return product


class ProductUpdateSerializer(serializers.Serializer):
    """
    A serializer can either implement create or update methods or both, as per django rest docs.
    Here we are using the update method as this serializer is designated for the PUT api
    We explicitly made all the parameters required=False, because we want the user to update
    the only properties they want to update
    """
    name = serializers.CharField(required=False,max_length=100)
    price = serializers.FloatField(required=False)
    quantity = serializers.IntegerField(required=False)
    delivery_cost = serializers.FloatField(required=False)
    ''' pk is the primary key, which is the row id, we want to output as field pk'''
    pk = serializers.SerializerMethodField()

    ''' Category is inputted as category_id of a pre-existing category'''
    category_id = serializers.IntegerField(required=False)

    ''' Company is inputted as company_id of a pre-existing company'''
    company_id = serializers.IntegerField(required=False)

    ''' Seller is inputted as seller_id of a pre-existing category'''
    seller_id = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        # checking if the foreign keys are valid
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            if not Category.objects.filter(pk=category_id).exists():
                raise serializers.ValidationError("Error: Category does not exist")
            else:
                instance.category_id = category_id

        if 'company_id' in validated_data:
            company_id = validated_data.pop('company_id')
            if not Company.objects.filter(pk=company_id).exists():
                raise serializers.ValidationError("Error: Company does not exist")
            else:
                instance.company_id = company_id

        if 'seller_id' in validated_data:
            seller_id = validated_data.pop('seller_id')
            if not User.objects.filter(pk=seller_id).exists():
                raise serializers.ValidationError("Error: Seller does not exist")
            else:
                instance.seller_id = seller_id

        ''' 
        Other fields we can update directly as they do not require any 
        validation for now
        '''
        if 'name' in validated_data:
            instance.name = validated_data.get('name', instance.name)
        if 'price' in validated_data:
            instance.price = validated_data.get('price', instance.price)
        if 'quantity' in validated_data:
            instance.quantity = validated_data.get('quantity', instance.quantity)
        if 'delivery_cost' in validated_data:
            instance.delivery_cost = validated_data.get('delivery_cost', instance.delivery_cost)
        instance.save()
        return instance

    def get_pk(self,obj):
        return obj.id


class ProductOutputSerializer(serializers.ModelSerializer):
    """
    pk is a generated field in serializer through SerializerMethodField,
    which is essentially the database primary key
    """
    pk = serializers.SerializerMethodField()

    ''' 
    Following fields are readyonly because we want them to output only, each of
    them causes corresponding foreign keys to output full object
    '''
    category = CategorySerializer(read_only=True)
    company = CompanyOutputSerializer(read_only=True)
    seller = SellerOutputSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'price','quantity', 'delivery_cost', 'category', 'company', 'seller', 'date', 'pk']

    def get_pk(self,obj):
        return obj.id
