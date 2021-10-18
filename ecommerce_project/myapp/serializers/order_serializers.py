import uuid

from rest_framework import serializers
from ecommerce_project.myapp.models import Product, BuyerUser, Order, OrderLine, Cart, CartLine
from ecommerce_project.myapp.serializers import BuyerOutputSerializer
from ecommerce_project.myapp.serializers.product_serializers import ProductOutputSerializer

order_output_fields = ['unique_order_id','buyer', 'date','value', 'billing_firstname', 'billing_lastname', 'billing_email', 'billing_contact_number','delivered','pk']


class OrderOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    buyer = BuyerOutputSerializer()

    class Meta:
        model = Order
        fields = order_output_fields

    def get_pk(self,obj):
        return obj.id


class OrderInputSerializer(serializers.ModelSerializer):
    buyer_user_id = serializers.IntegerField(required=True)
    billing_firstname = serializers.CharField(required=True, max_length=100)
    billing_lastname = serializers.CharField(required=True, max_length=100)
    billing_email = serializers.CharField(required=True, max_length=100)
    billing_contact_number = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Order
        fields = ['buyer_user_id', 'billing_firstname', 'billing_lastname', 'billing_email', 'billing_contact_number', 'value','delivered']

    def create(self, validated_data):
        buyer_user_id = validated_data.pop('buyer_user_id')
        order = Order.objects.create(**validated_data)
        order.unique_order_id = uuid.uuid4().hex[:6].upper()
        order.save()

        try:
            buyer_user = BuyerUser.objects.get(pk=buyer_user_id)
        except BuyerUser.DoesNotExist:
            raise serializers.ValidationError("userError: problem with the user for this order.")
        order.buyer = buyer_user

        order.save()
        #now move the cartlines to orderlines ,associate with this order and remove cartlines
        user_cart = Cart.objects.get(user_id=buyer_user_id)
        cartlines = CartLine.objects.filter(cart_id=user_cart.id)
        if cartlines:
            #means not empty, means there are cartlines
            for cartline in cartlines:
                orderline = OrderLine.objects.create(order_id=order.id, product_id=cartline.product.id,quantity=cartline.quantity)
            #now delete the cartlines
            CartLine.objects.filter(cart_id=user_cart.id).delete()
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
    billing_firstname = serializers.CharField(required=False, max_length=100)
    billing_lastname = serializers.CharField(required=False, max_length=100)
    billing_email = serializers.CharField(required=False, max_length=100)
    billing_contact_number = serializers.CharField(required=False, max_length=100)
    pk = serializers.SerializerMethodField()
    """
    A serializer can either implement create or update methods or both, as per django rest docs. 
    """
    def update(self, instance, validated_data):

        if 'value' in validated_data:
            instance.value = validated_data.get('value', instance.value)
        if 'billing_firstname' in validated_data:
            instance.billing_firstname = validated_data.get('billing_firstname', instance.billing_firstname)
        if 'billing_lastname' in validated_data:
            instance.billing_lastname = validated_data.get('billing_lastname', instance.billing_lastname)
        if 'billing_email' in validated_data:
            instance.billing_email = validated_data.get('billing_email', instance.billing_email)
        if 'billing_contact_number' in validated_data:
            instance.billing_contact_number = validated_data.get('billing_contact_number', instance.billing_contact_number)
        if 'delivered' in validated_data:
            instance.delivered = validated_data.get('delivered', instance.delivered)
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


class OrderWithLinesForUserOutputSerializer(serializers.ModelSerializer):
    #just adding cartlines won't work, if you do not specify related name
    # as cartlines in the cartline model
    orderlines = OrderLineOutputSerializer(many=True, read_only=True)
    buyer = BuyerOutputSerializer()
    pk = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()

    class Meta:
        order_outputs_extended = order_output_fields.copy()
        order_outputs_extended.extend(['orderlines','quantity'])
        # print(order_outputs_extended)
        model = Order
        fields = order_outputs_extended
        # fields = ['unique_order_id','buyer', 'date','value', 'billing_firstname', 'billing_lastname', 'billing_email', 'billing_contact_number','delivered','orderlines','quantity','pk']

    def get_pk(self,obj):
        return obj.id

    def get_quantity(self,obj):
        order_object = obj
        orderlines = OrderLine.objects.filter(order_id=order_object.id)
        total_quantity = 0
        for orderline in orderlines:
            total_quantity = total_quantity + orderline.quantity
        return total_quantity