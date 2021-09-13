from django.contrib import admin
from .models import Category, Product, ProductImage
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Product)
admin.site.register(ProductImage)