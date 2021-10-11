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


class CartOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    user = BuyerOutputSerializer()

    class Meta:
        model = Cart
        fields = ['unique_id', 'user', 'pk']

    def get_pk(self,obj):
        return obj.id


class CartInputSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Cart
        fields = ['user_id', 'unique_id']
        required_spec_dict = {
            'required': True,
            'allow_blank': False
        }
        # This will force a field in the userinput to make it required, even if
        # the corresponding model field is not required/null=true
        extra_kwargs = {
            'unique_id': required_spec_dict
        }

    def create(self, validated_data):
        #the trick here is, we made the user field optional so the serializer donn't keep
        #asking for that as required field. The user is already created before, so it makes
        #no sense to send user profile in the payload, only user id is enough
        #so, we add an extra field in the api payload, which will be cut
        # and then cart will be created and we later associate the user with this id in the cart
        user_id = validated_data.pop('user_id')

        try:
            buyer_user = BuyerUser.objects.get(pk=user_id)
        except BuyerUser.DoesNotExist:
            raise serializers.ValidationError("userError: problem with the user for this cart.")
        if Cart.objects.filter(user=buyer_user).exists():
            raise serializers.ValidationError("userError: Cart already exists for the user")
        else:
            cart = Cart.objects.create(**validated_data)
            cart.user = buyer_user

        cart.save()
        return cart


class CartLineOutputSerializer(serializers.ModelSerializer):
    pk = serializers.SerializerMethodField()
    product = ProductOutputSerializer()
    cart = CartOutputSerializer()

    class Meta:
        model = OrderLine
        fields = ['product', 'cart', 'quantity', 'pk']

    def get_pk(self,obj):
        return obj.id


class CartLineInputSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(required=True)
    cart_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = CartLine
        fields = ['product_id', 'cart_id','quantity']

    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        cart_id = validated_data.pop('cart_id')

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("productError: problem with the product for this carline.")

        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("cartError: problem with the cart for this cartline.")

        if CartLine.objects.filter(cart=cart, product = product).exists():
            raise serializers.ValidationError("cartError: This cartline for the product and the cart already exists, update instead of creating")
        else:
            cartline = CartLine.objects.create(**validated_data)
            cartline.product = product
            cartline.cart = cart

        cartline.save()
        return cartline
