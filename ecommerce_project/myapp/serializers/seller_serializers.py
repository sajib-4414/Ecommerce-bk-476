from rest_framework import serializers
from ecommerce_project.myapp.models import SellerUser


class SellerOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    photo_id_num = serializers.CharField(source='photoIdNum')  # Changing the model's name

    class Meta:
        model = SellerUser
        fields = ('name', 'email','photo_id_num', 'pk')

    def get_pk(self,obj):
        return obj.id


class SellerInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    photo_id_num = serializers.CharField(source='photoIdNum') #Changing the model's name in API input field

    class Meta:
        model = SellerUser
        fields = ('name', 'email', 'password','photo_id_num')

    def create(self, validated_data):
        user = SellerUser.objects.create(**validated_data)
        return user