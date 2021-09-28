from django.contrib import admin
from ecommerce_project.myapp.models import BuyerUser, Address, Company, Category, Product

admin.site.register(BuyerUser)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product)