from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        data = self.street_address
        return data


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.seller = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    photoIdNum = models.CharField(max_length=50,null=True,blank=True)
    # email = models.CharField(max_length=50)
    # username = models.CharField(max_length=30)
    # password = models.CharField(max_length=30)
    address = models.OneToOneField(
        Address,
        on_delete=models.DO_NOTHING,
        related_name='address_user_of',
        null=True,
        blank=True
    )

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " "+ self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):
        return self.get_full_name()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    objects = UserManager()



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
    # user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=None)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.OneToOneField(
        Address,
        on_delete=models.DO_NOTHING,
        related_name='address_of',
        null=True
    )

    def __str__(self):
        data = self.first_name + ' '+ self.last_name
        return data


class SellerUser(models.Model):
    # user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=None)
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
        on_delete=models.DO_NOTHING,
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

from django.contrib.auth import get_user_model
User = get_user_model()

class Review(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_done_by', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews_of', null=True)

    def __str__(self):
        data = (self.description[:25] + '..') if len(self.description) > 25 else self.description
        return data


class Cart(models.Model):
    unique_id = models.CharField(max_length=50, null=True)
    # products = models.ManyToManyField(Product, related_name='carts_where_this_product', blank=True)
    # cart_lines = models.ForeignKey(CartLine, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        data = self.unique_id
        return data


class CartLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name= 'cartlines', null=True, blank=True)
    quantity = models.IntegerField(default=1)

    # def __str__(self):
    #     return "Cart item of " + self.cart.unique_id

class Order(models.Model):
    unique_order_id = models.CharField(null=True,max_length=100)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_of', null=True)
    # products = models.ManyToManyField(Product, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    value = models.FloatField()
    billing_firstname = models.CharField(max_length=100, null=True)
    billing_lastname = models.CharField(max_length=100, null=True)
    billing_email = models.CharField(max_length=100, null=True)
    billing_contact_number = models.CharField(max_length=100, null=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        data = self.unique_order_id
        return data


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderlines', null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Order item of the product" + self.product.name


