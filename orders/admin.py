from django.contrib import admin
from .models import Order, OrderRow, OrderHistory, DiscountCode

admin.site.register(Order)
admin.site.register(OrderRow)
admin.site.register(OrderHistory)
admin.site.register(DiscountCode)