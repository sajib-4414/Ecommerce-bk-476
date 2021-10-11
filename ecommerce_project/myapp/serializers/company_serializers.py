from rest_framework import serializers
from ecommerce_project.myapp.models import Address, Company
from ecommerce_project.myapp.serializers.other_serializers import AddressSerializer


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

class CompanyUpdateSerializer(serializers.Serializer):
    company_name = serializers.CharField(required=False,max_length=100)
    company_username = serializers.CharField(max_length=50,required=False)
    address = AddressSerializer(required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):

        if 'company_name' in validated_data:
            instance.company_name = validated_data.get('company_name', instance.company_name)
        if 'company_username' in validated_data:
            instance.company_username = validated_data.get('company_username', instance.company_username)

        if 'address' in validated_data:
            address_data = validated_data.pop('address')
            #check if the user already have an address
            try:
                existing_address = Company.objects.get(pk=instance.id).address
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