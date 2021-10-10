from rest_framework import serializers
from ecommerce_project.myapp.models import BuyerUser, SellerUser, Address
from ecommerce_project.myapp.serializers.OtherSerializers import AddressOutputSerializer


class BuyerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    address = AddressOutputSerializer()

    class Meta:
        model = BuyerUser
        fields = ['full_name', 'email','username','address','pk']

    def get_pk(self,obj):
        return obj.id


class SellerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    photo_id_num = serializers.CharField(source='photoIdNum')  # Changing the model's name

    class Meta:
        model = SellerUser
        fields = ('name', 'email','photo_id_num', 'pk')

    def get_pk(self,obj):
        return obj.id


class BuyerInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = AddressOutputSerializer()

    class Meta:
        model = BuyerUser
        fields = ('full_name', 'email', 'username', 'password','address')
        required_spec_dict = {
            'required': True,
            'allow_blank': False
        }

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = BuyerUser.objects.create(**validated_data)
        address = Address.objects.create(**address_data)
        user.address = address
        user.save()
        return user


class SellerInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    photo_id_num = serializers.CharField(source='photoIdNum') #Changing the model's name in API input field

    class Meta:
        model = SellerUser
        fields = ('name', 'email', 'password','photo_id_num')

    def create(self, validated_data):
        user = SellerUser.objects.create(**validated_data)
        return user