from django.urls import path, include

urlpatterns = [
    path('users/', include('customers.api.urls')),
    path('products/', include('products.api.urls')),
    path('orders/', include('orders.api.urls')),
]
