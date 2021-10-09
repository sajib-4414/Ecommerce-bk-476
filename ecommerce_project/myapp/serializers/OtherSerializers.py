from rest_framework import serializers
from ecommerce_project.myapp.models import Address


class AddressOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'