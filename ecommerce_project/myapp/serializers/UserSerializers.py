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
    class Meta:
        model = SellerUser
        fields = '__all__'


class BuyerInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_id = serializers.SerializerMethodField('get_user_id')
    address = AddressOutputSerializer()

    # image = ImageSerializer(required=False)  # If you write here ImageSerializer then serializer will expect an integer(which)
    # # is primary key here in the payload and also output the same, if you write here ImageSerializer() then the payload
    # # have to contain dict and also output the image as dict

    def get_user_id(self, obj):
        return obj.id

    class Meta:
        model = BuyerUser
        fields = ('full_name', 'email', 'username', 'password','address','user_id')
        required_spec_dict = {
            'required': True,
            'allow_blank': False
        }
        # extra_kwargs = {
        #     'email': required_spec_dict
        # }
        # expandable_fields = {
        #     'image': (ImageSerializer, {'many': False}),
        # }

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = BuyerUser.objects.create(**validated_data)
        address = Address.objects.create(**address_data)
        user.address = address
        user.save()
        return user

        # user = super(BuyerInputSerializer, self).create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()
        # return user
