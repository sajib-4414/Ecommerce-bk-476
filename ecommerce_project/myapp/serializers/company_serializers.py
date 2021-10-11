from rest_framework import serializers
from ecommerce_project.myapp.models import Address, Company
from ecommerce_project.myapp.serializers.OtherSerializers import AddressSerializer


class CompanyOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    address = AddressSerializer()
    company_name = serializers.CharField(source='CompanyName')  # Changing the model's name

    class Meta:
        model = Company
        fields = ('company_name', 'company_username','address', 'pk')

    def get_pk(self,obj):
        return obj.id


class CompanyInputSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
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