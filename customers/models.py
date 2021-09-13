from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator


class ShopUser(User):
    identity_code = models.CharField(max_length=10, unique=True, validators=[
        RegexValidators(
            regex='\b[0-9]{10}\b',
            message='entity code must be 10 digits',
            code='invalid_entity_code'
        )])
    age = models.PositiveIntegerField(validators=[MinValueValidator(5)])
    gender_choices = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = models.CharField(choices=gender_choices, max_length=20)
    phone_number = models.CharField(max_length=15, unique=True)


class Customer(ShopUser):
    is_customer = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class CustomerImage(models.Model):
    customer = models.ForeignKey(Customer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image/customers', default=None, null=True)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} profile image'

    class Meta:
        verbose_name = 'Customer image'
        verbose_name_plural = 'Customer images'


class Employee(ShopUser):
    is_employee = True
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_title = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image/employees', default=None, null=True)

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name} profile image'

    class Meta:
        verbose_name = 'Employee image'
        verbose_name_plural = 'Employee images'


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    alley = models.CharField(max_length=30)
    no = models.PositiveIntegerField()
    postal_code = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} address'

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
