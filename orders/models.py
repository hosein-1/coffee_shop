from django.db import models
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='نام گیرنده')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی گیرنده')
    phone_number = models.CharField(max_length=15, verbose_name='شماره تلفن')
    province = models.CharField(max_length=100, verbose_name='استان')
    city = models.CharField(max_length=100, verbose_name='شهر')
    address = models.CharField(max_length=700, blank=True)
    postal_code = models.CharField(max_length=20, verbose_name='کدپستی')
    is_paid = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        # result = 0
        # for item in self.items.all():
        #     result += item.price * item.quantity

        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id} of {self.order.id}'
