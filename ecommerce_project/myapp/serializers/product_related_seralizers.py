from rest_framework import serializers

from ecommerce_project.myapp.models import Product
from ecommerce_project.myapp.serializers.OtherSerializers import CategorySerializer
from ecommerce_project.myapp.serializers.UserSerializers import CompanyOutputSerializer, SellerOutputSerializer


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