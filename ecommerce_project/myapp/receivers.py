from django.dispatch import receiver
from ecommerce_project.myapp import signals
from ecommerce_project.myapp.models import Order, Product, OrderLine


@receiver(signals.order_confirmed)
def my_task_done(sender, order_id, **kwargs):
    print("Observer Noted order finished, order ID is::"+str(order_id))
    # now decrease the product quantity of the ordered products
    # order_id = 18
    order = Order.objects.get(pk=order_id)
    print("printing order object")
    print(order)
    orderlines = OrderLine.objects.filter(order_id=order_id)
    if orderlines:
        print("queryset not empty")
    else:
        print("queryset empty!!!!!!!!!!!")
    for orderline in orderlines:
        product = Product.objects.get(pk=orderline.product.id)
        quantity = product.quantity - orderline.quantity
        if quantity >=0:
            product.quantity = quantity
        else:
            product.quantity = 0
        print("lastly updating the quanttity now")
        product.save()