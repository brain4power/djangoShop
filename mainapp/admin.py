from django.contrib import admin
from .models import Product, Gender, Category, MenuCategory, Brand, Size


# Register your models here.

admin.site.register(Product)
admin.site.register(Gender)
admin.site.register(Category)
admin.site.register(MenuCategory)
admin.site.register(Brand)
admin.site.register(Size)
