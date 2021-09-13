from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class ShopUser(User):
    identity_code = models.PositiveBigIntegerField(unique=True,
                                                   validators=[MinLengthValidator(9), MaxLengthValidator(10)])
    phone_number = models.TextField(max_length=15, unique=True)


class Customer(ShopUser):
    is_customer = True


class CustomerImage(models.Model):
    customer = models.ForeignKey(Customer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image/customers', default=None, null=True)


class Employee(ShopUser):
    is_employee = True
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()


class EmployeeImage(models.Model):
    Employee = models.ForeignKey(Employee, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image/employees', default=None, null=True)


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    alley = models.CharField(max_length=30)
    no = models.PositiveIntegerField()
    postal_code = models.PositiveBigIntegerField()
