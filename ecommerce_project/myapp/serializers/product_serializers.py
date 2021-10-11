from rest_framework import serializers

from ecommerce_project.myapp.models import Category, Company, SellerUser


class ProductUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False,max_length=100)
    price = serializers.FloatField(required=False)
    quantity = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(required=False)
    company_id = serializers.IntegerField(required=False)
    seller_id = serializers.IntegerField(required=False)
    delivery_cost = serializers.FloatField(required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):
        if 'category_id' in validated_data:
            #wants to update category, have to check if the category is a valid one
            category_id = validated_data.pop('category_id')
            try:
                category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                raise serializers.ValidationError("categoryError: problem with the user for this product.")
            instance.category = category

        if 'company_id' in validated_data:
            #wants to update company, have to check if the company is a valid one
            company_id = validated_data.pop('company_id')
            try:
                company = Company.objects.get(pk=company_id)
            except Company.DoesNotExist:
                raise serializers.ValidationError("companyError: problem with the company for this product.")
            instance.company = company

        if 'seller_id' in validated_data:
            # wants to update seller, have to check if the seller is a valid one
            seller_id = validated_data.pop('seller_id')
            try:
                seller = SellerUser.objects.get(pk=seller_id)
            except SellerUser.DoesNotExist:
                raise serializers.ValidationError("sellerError: problem with the seller for this product.")
            instance.seller = seller

        if 'name' in validated_data:
            instance.name = validated_data.get('name', instance.name)
        if 'price' in validated_data:
            instance.price = validated_data.get('price', instance.price)
        if 'quantity' in validated_data:
            instance.quantity = validated_data.get('quantity', instance.quantity)
        if 'delivery_cost' in validated_data:
            instance.delivery_cost = validated_data.get('delivery_cost', instance.delivery_cost)
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