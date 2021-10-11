from rest_framework import serializers

from ecommerce_project.myapp.models import BuyerUser, Address
from ecommerce_project.myapp.serializers.other_serializers import AddressSerializer


class BuyerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    address = AddressSerializer()

    class Meta:
        model = BuyerUser
        fields = ['full_name', 'email','username','address','pk']

    def get_pk(self,obj):
        return obj.id


class BuyerInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = AddressSerializer()

    class Meta:
        model = BuyerUser
        fields = ('full_name', 'email', 'username', 'password','address')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = BuyerUser.objects.create(**validated_data)
        address = Address.objects.create(**address_data)
        user.address = address
        user.save()
        return user