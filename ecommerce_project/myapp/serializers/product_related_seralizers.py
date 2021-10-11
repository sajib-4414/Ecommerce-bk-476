from rest_framework import serializers
from ecommerce_project.myapp.models import Product, BuyerUser, Order, OrderLine, \
    Cart, CartLine
from ecommerce_project.myapp.serializers.UserSerializers import \
    BuyerOutputSerializer
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

