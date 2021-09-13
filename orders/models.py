from random import randint

from django.db import models
from customers.models import Customer
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


def auto_generate_order_code():
    generated_order_code = str(randint(1000000000, 9999999999))
    if Order.objects.filter(code=generated_order_code).count() == 0:
        return generated_order_code
    else:
        auto_generate_order_code()


class Order(models.Model):
    code = models.CharField(default=auto_generate_order_code, max_length=15)
    date = models.DateTimeField(auto_now=True)
    status_code = (
        ('1', 'submitted'),
        ('2', 'canceled'),
        ('3', 'sent'),
        # ('4', 'delivered')
    )
    status = models.CharField(choices=status_code, default='1', max_length=15)
    note = models.TextField(max_length=200, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'order code: {self.code}, status: {self.status}'


class OrderRow(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'a row from order No. {self.order.code}'


class OrderHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)

    def __str__(self):
        return f'order No. {self.order.code} for {self.customer.first_name} {self.customer.last_name}'


class DiscountCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    percent = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    start = models.DateTimeField()
    end = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'discount code for {self.customer.first_name} {self.customer.last_name}'
