from django.db import models


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        data = self.street_address
        return data


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        data = self.name
        return data


class BuyerUser(models.Model):
    """
    delete dependencies upon object deletion
    pending
    """
    full_name = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name='address_of',
        null=True
    )

    def __str__(self):
        data = self.full_name
        return data


class SellerUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    photoIdNum = models.CharField(max_length=50)

    def __str__(self):
        data = self.name
        return data


class Company(models.Model):
    CompanyName = models.CharField(max_length=100)
    company_username = models.CharField(max_length=50,null=True)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name='company_address_of',
        null=True
    )

    def __str__(self):
        data = self.CompanyName
        return data


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_of',
        null=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='company_of',
        null=True
    )
    seller = models.ForeignKey(
        SellerUser,
        on_delete=models.CASCADE,
        related_name='seller_of',
        null=True
    )
    delivery_cost = models.FloatField()
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        data = self.name
        return data


class Review(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(BuyerUser, on_delete=models.CASCADE, related_name='reviews_of')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews_of', null=True)

    def __str__(self):
        data = (self.description[:25] + '..') if len(self.description) > 25 else self.description
        return data


class Cart(models.Model):
    unique_id = models.CharField(max_length=50, null=True)
    # products = models.ManyToManyField(Product, related_name='carts_where_this_product', blank=True)
    # cart_lines = models.ForeignKey(CartLine, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(BuyerUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        data = self.unique_id
        return data


class CartLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Cart item of " + self.product.name


class Order(models.Model):
    buyer = models.ForeignKey(BuyerUser, on_delete=models.CASCADE, related_name='orders_of')
    # products = models.ManyToManyField(Product, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    value = models.FloatField()

    def __str__(self):
        data = "Order of buyer "+ self.buyer.full_name
        return data


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Order item of the product" + self.product.name