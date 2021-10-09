from rest_framework import serializers

from ecommerce_project.myapp.models import BuyerUser
from ecommerce_project.myapp.serializers.OtherSerializers import AddressOutputSerializer


class BuyerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    address = AddressOutputSerializer()

    class Meta:
        model = BuyerUser
        fields = ['full_name', 'email','username','address','pk']

    def get_pk(self,obj):
        return obj.id
