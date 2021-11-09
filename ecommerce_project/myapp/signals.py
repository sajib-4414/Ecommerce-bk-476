from django import dispatch
from django.db.models.signals import post_save
from django.dispatch import receiver
from ecommerce_project.myapp.models import Product, OrderLine, Cart
from django.contrib.auth import get_user_model
User = get_user_model()


"""
This observer method observes whether a new user is created, then a cart object is created
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("Observer:: A new user is created. A cart will be autocreated for him")
        if not Cart.objects.filter(user_id=instance.id).exists():
            # no cart exists, we will create a new cart for the user
            Cart.objects.create(user_id=instance.id)



"""
This receiver or observer observes the Product value changes event
in that event it updates all the associated order totals
"""
@receiver(post_save, sender=Product)
def product_changed(sender, instance, **kwargs):
    print("Observer:: product updated...")
    orderlines_with_this_product = OrderLine.objects.filter(product_id=instance.id)
    if orderlines_with_this_product:
        for orderline in orderlines_with_this_product:
            order = orderline.order
            '''
            calculating new total and saving it
            '''
            total = sum(ordl.total for ordl in order.orderlines.all())
            order.value = total
            order.save()

"""
This is a custom observer method which observes when a signal named order_confirmed
is manually fired. This is not a built in signal found in django.
"""
order_confirmed = dispatch.Signal(providing_args=["order_id","cart_id"])

# @receiver(post_init, sender=User)
# def post_init_called(sender, **kwargs):
#     print("I am fired")