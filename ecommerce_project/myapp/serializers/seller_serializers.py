from rest_framework import serializers
from ecommerce_project.myapp.models import SellerUser

from django.contrib.auth import get_user_model
User = get_user_model()


class SellerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    photo_id_num = serializers.CharField(source='photoIdNum')  # Changing the model's name
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('name', 'email','photo_id_num', 'pk')

    def get_pk(self,obj):
        return obj.id

    def get_name(self,obj):
        return obj.first_name+" "+obj.last_name


class SellerInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    photo_id_num = serializers.CharField(source='photoIdNum') #Changing the model's name in API input field

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password','photo_id_num')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.staff=False
        user.admin=True
        return user

class AddressUpdateSerializer(serializers.Serializer):
    street_address = serializers.CharField(required=False,max_length=100)
    city = serializers.CharField(max_length=20,required=False)
    province = serializers.CharField(max_length=20, required=False)
    zipcode = serializers.CharField(max_length=10, required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):
        if 'street_address' in validated_data:
            instance.street_address = validated_data.get('street_address', instance.street_address)
        if 'city' in validated_data:
            instance.city = validated_data.get('city', instance.city)
        if 'province' in validated_data:
            instance.province = validated_data.get('province', instance.province)
        if 'zipcode' in validated_data:
            instance.zipcode = validated_data.get('zipcode', instance.zipcode)

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


class SellerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=False)
    last_name = serializers.CharField(max_length=200, required=False)
    email = serializers.CharField(max_length=30, required=False)
    password = serializers.CharField(max_length=50, required=False)
    photo_id_num = serializers.CharField(max_length=50, required=False)
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
        if 'password' in validated_data:
            instance.password = validated_data.get('password', instance.password)
        if 'photo_id_num' in validated_data:
            instance.photoIdNum = validated_data.get('photo_id_num', instance.photoIdNum)
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

    def get_pk(self, obj):
        return obj.id

