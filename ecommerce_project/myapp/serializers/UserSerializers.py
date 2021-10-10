from rest_framework import serializers
from ecommerce_project.myapp.models import BuyerUser, SellerUser, Address, Company
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


class CompanyOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    address = AddressOutputSerializer()
    company_name = serializers.CharField(source='CompanyName')  # Changing the model's name

    class Meta:
        model = Company
        fields = ('company_name', 'company_username','address', 'pk')

    def get_pk(self,obj):
        return obj.id


class CompanyInputSerializer(serializers.ModelSerializer):
    address = AddressOutputSerializer()
    company_name = serializers.CharField(source='CompanyName')

    class Meta:
        model = Company
        fields = ('company_name', 'company_username','address')
        required_spec_dict = {
            'required': True,
            'allow_blank': False
        }
        #This will force a field in the userinput to make it required, even if
        #the corresponding model field is not required/null=true
        extra_kwargs = {
            'company_username': required_spec_dict
        }

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        company = Company.objects.create(**validated_data)
        address = Address.objects.create(**address_data)
        company.address = address
        company.save()
        return company