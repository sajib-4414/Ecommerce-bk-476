from rest_framework import serializers

from ecommerce_project.myapp.models import BuyerUser, Address
from ecommerce_project.myapp.serializers.other_serializers import AddressSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class BuyerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username','address','pk']

    def get_pk(self,obj):
        return obj.id


class BuyerInputSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(write_only=True)
    address = AddressSerializer(required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'username', 'password','address')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = User.objects.create(**validated_data)
        address = Address.objects.create(**address_data)
        user.address = address
        user.save()
        return user


class BuyerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False,max_length=100)
    last_name = serializers.CharField(required=False, max_length=100)
    email = serializers.CharField(max_length=50,required=False)
    username = serializers.CharField(max_length=30,required=False)
    password = serializers.CharField(max_length=30, write_only=True, required=False)
    address = AddressSerializer(required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):

        if 'first_name' in validated_data:
            instance.first_name = validated_data.get('first_name', instance.first_name)
        if 'last_name' in validated_data:
            instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'email' in validated_data:
            instance.email = validated_data.get('email', instance.email)
        if 'username' in validated_data:
            instance.username = validated_data.get('username', instance.username)
        if 'password' in validated_data:
            instance.set_password(validated_data.get('password'))
        if 'address' in validated_data:
            address_data = validated_data.pop('address')
            #check if the user already have an address
            try:
                existing_address = BuyerUser.objects.get(pk=instance.id).address
                existing_address.street_address = address_data.get('street_address')
                existing_address.city = address_data.get('city')
                existing_address.province = address_data.get('province')
                existing_address.zipcode = address_data.get('zipcode')
                existing_address.save()
            except Address.DoesNotExist:
                new_address = Address.objects.create(**address_data)
                instance.address = new_address


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