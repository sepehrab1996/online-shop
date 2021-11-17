from django.contrib import admin
from .models import Customer, Employee, Address, CustomerImage, EmployeeImage

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Address)
admin.site.register(CustomerImage)
admin.site.register(EmployeeImage)
