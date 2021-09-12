from django.db import models
from django.contrib.auth.models import User
from orders.models import DiscountCode


class ShopUser(User):
    identity_code = models.PositiveBigIntegerField(unique=True)
    phone_number = models.TextField(max_length=20, unique=True)
    profile_image = models.ImageField(upload_to='profile_image', default=None, null=True)


