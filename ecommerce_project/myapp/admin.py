from django.contrib import admin

# Register your models here.
from ecommerce_project.myapp.models import BuyerUser, Address

admin.site.register(BuyerUser)
admin.site.register(Address)