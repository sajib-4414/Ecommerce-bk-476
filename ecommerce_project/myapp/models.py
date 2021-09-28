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
    )

    def __str__(self):
        data = self.full_name
        return data


class Company(models.Model):
    CompanyName = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name='company_address_of',
    )

    def __str__(self):
        data = self.CompanyName
        return data


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        related_name='category_of',
    )
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name='company_of',
    )
    delivery_cost = models.FloatField()

    def __str__(self):
        data = self.name
        return data