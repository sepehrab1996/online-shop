from django.urls import path, include
from .views import CustomerRegister

urlpatterns = [
    # path('customer_image/<int:pk>/', CustomerImageDetail.as_view(), name='api-customer-image-detail'),
    # path('', CustomerList.as_view(), name='api-customer-list'),
    path('register/', CustomerRegister.as_view(), name='api-customer-register'),
]
