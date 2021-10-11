from rest_framework import serializers
from ecommerce_project.myapp.models import Product, BuyerUser, Order, OrderLine
from ecommerce_project.myapp.serializers import BuyerOutputSerializer
from ecommerce_project.myapp.serializers.product_serializers import ProductOutputSerializer


class OrderOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    buyer = BuyerOutputSerializer()

    class Meta:
        model = Order
        fields = ['buyer', 'date','value', 'pk']

    def get_pk(self,obj):
        return obj.id


class OrderInputSerializer(serializers.ModelSerializer):
    buyer_user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Order
        fields = ['buyer_user_id', 'value']

    def create(self, validated_data):
        buyer_user_id = validated_data.pop('buyer_user_id')
        order = Order.objects.create(**validated_data)

        try:
            buyer_user = BuyerUser.objects.get(pk=buyer_user_id)
        except BuyerUser.DoesNotExist:
            raise serializers.ValidationError("userError: problem with the user for this order.")
        order.buyer = buyer_user

        order.save()
        return order


class OrderLineOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    product = ProductOutputSerializer()
    order = OrderOutputSerializer()

    class Meta:
        model = OrderLine
        fields = ['product', 'quantity', 'order', 'pk']

    def get_pk(self,obj):
        return obj.id


class OrderLineInputSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(required=True)
    order_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = OrderLine
        fields = ['product_id', 'order_id','quantity']

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        order_id = validated_data.pop('order_id')
        orderline = OrderLine.objects.create(**validated_data)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("productError: problem with the product for this orderline.")
        orderline.product = product

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            raise serializers.ValidationError("orderError: problem with the order for this orderline.")
        orderline.order = order

        orderline.save()
        return orderline


class OrderUpdateSerializer(serializers.Serializer):
    value = serializers.FloatField(required=False)
    buyer_id = serializers.IntegerField(required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):

        if 'value' in validated_data:
            instance.value = validated_data.get('value', instance.value)
        if 'buyer_id' in validated_data:
            #wants to update user, have to check if the user is a valid one
            buyer_id = validated_data.pop('buyer_id')
            try:
                buyer_user = BuyerUser.objects.get(pk=buyer_id)
            except BuyerUser.DoesNotExist:
                raise serializers.ValidationError("userError: problem with the user for this order.")
            instance.user = buyer_user

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


class OrderLineUpdateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(required=False)
    order_id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField(required=False)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):
        if 'product_id' in validated_data:
            #wants to update product, have to check if the product is a valid one
            product_id = validated_data.pop('product_id')
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("productError: problem with the product for this orderline.")
            instance.product = product

        if 'order_id' in validated_data:
            #wants to update order, have to check if the cart is a valid one
            order_id = validated_data.pop('order_id')
            try:
                order = Order.objects.get(pk=order_id)
            except Order.DoesNotExist:
                raise serializers.ValidationError("orderError: problem with the order for this orderline.")
            instance.order = order

        if 'quantity' in validated_data:
            supplied_quantity = validated_data.get('quantity', instance.quantity)
            if supplied_quantity <=0:
                raise serializers.ValidationError("quantityError: problem with the quantity for this cartline.")
            instance.quantity = supplied_quantity
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

