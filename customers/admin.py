from django.contrib import admin
from .models import Customer, Employee, Address


admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Address)