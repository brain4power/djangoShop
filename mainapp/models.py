from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# blank = True, null = True


class Gender(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    quick_overview = models.TextField()
    full_description = models.TextField()
    additional_information = models.TextField()
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    length = models.IntegerField()
    # есть пара сигналов во views orderapp
    quantity = models.IntegerField()
    reviews = models.IntegerField()
    image = models.ImageField(upload_to="products", blank=True, null=True)
    is_active = models.BooleanField(verbose_name='категория активна', default=True)

    def __str__(self):
        return self.name
