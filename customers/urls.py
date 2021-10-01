from django.urls import path, include
from customers.views import ShowCustomerRegisterForm

urlpatterns = [
    path('register/', ShowCustomerRegisterForm.as_view(), name='show-customer-register-form'),
]
