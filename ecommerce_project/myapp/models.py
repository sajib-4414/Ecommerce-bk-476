from django.db import models


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        data = self.street_address
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
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        data = self.full_name
        return data



