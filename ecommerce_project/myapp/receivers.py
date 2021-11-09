from django.dispatch import receiver
from ecommerce_project.myapp import signals
from ecommerce_project.myapp.models import Order, Product, OrderLine, CartLine, Cart

"""
This is the receiver of a manually defined Signal Observer.
It is fired when this specific signal is fired by anywhere in the code
It aims to remove same blocks of code from multiple places
"""
@receiver(signals.order_confirmed)
def my_task_done(sender, order_id, cart_id, **kwargs):
    print("Observer Noted order finished, order ID is::"+str(order_id)+", cart ID is::"+str(cart_id))

    '''
    We got a signal order complete, so we will decrease the products quantity and delete the cart
    items here
    '''
    order = Order.objects.get(pk=order_id)
    orderlines = OrderLine.objects.filter(order_id=order_id)
    for orderline in orderlines:
        product = Product.objects.get(pk=orderline.product.id)
        quantity = product.quantity - orderline.quantity
        if quantity >=0:
            product.quantity = quantity
        else:
            product.quantity = 0
        product.save()

    # now removing the cart items
    CartLine.objects.filter(cart_id=cart_id).delete()
