from django.db import models
from django.contrib.auth.models import User
from orders.models import DiscountCode


class ShopUser(User):
    identity_code = models.PositiveBigIntegerField(unique=True)
    phone_number = models.TextField(max_length=20, unique=True)
    profile_image = models.ImageField(upload_to='profile_image', default=None, null=True)


class Customer(ShopUser):
    is_customer = True
    address = models.OneToOneField("Address", on_delete=models.CASCADE)
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE)


class Employee(ShopUser):
    is_employee = True
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()



