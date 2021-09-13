from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Product)
