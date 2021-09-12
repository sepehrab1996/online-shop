from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField(default=None)
    inventory = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='product_image')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
