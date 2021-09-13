from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField(default=None)
    inventory = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200, null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ${self.price}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image', default=None, null=True)

    def __str__(self):
        return f'{self.product.name} image'


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']
