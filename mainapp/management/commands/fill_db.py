from django.core.management.base import BaseCommand
from mainapp.models import Gender, Category, MenuCategory, Brand, Size, Product
from django.contrib.auth.models import User

import json
import os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        gender = loadFromJSON('genders')

        Gender.objects.all().delete()
        for category in gender:
            new_category = Gender(**category)
            new_category.save()

        categories = loadFromJSON('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        menu_category = loadFromJSON('menu_categories')
        MenuCategory.objects.all().delete()
        for category in menu_category:
            new_category = MenuCategory(**category)
            new_category.save()

        brand = loadFromJSON('brands')
        Brand.objects.all().delete()
        for category in brand:
            new_category = Brand(**category)
            new_category.save()

        size = loadFromJSON('sizes')
        Size.objects.all().delete()
        for category in size:
            new_category = Size(**category)
            new_category.save()

        products = loadFromJSON('products')
        Product.objects.all().delete()
        for product in products:
            # заменяем пол на объект:
            gender_name = product["gender"]
            _gender = Gender.objects.get(name=gender_name)
            product["gender"] = _gender
            # заменяем категорию на объект:
            category_name = product["category"]
            _category = Category.objects.get(name=category_name)
            product["category"] = _category
            # заменяем меню_категорию на объект:
            menu_category_name = product["menu_category"]
            _menu_category = MenuCategory.objects.get(name=menu_category_name)
            product["menu_category"] = _menu_category
            # заменяем бренд на объект:
            brand_name = product["brand"]
            _brand = Brand.objects.get(name=brand_name)
            product["brand"] = _brand
            # заменяем размер на объект:
            size_name = product["size"]
            _size = Size.objects.get(name=size_name)
            product["size"] = _size
            # пихаем все в Product и сохраняем:
            new_product = Product(**product)
            new_product.save()

        # User.objects.all().delete()
        # Создаем суперпользователя при помощи менеджера модели
        # super_user = User.objects.create_superuser('admin', 'yotakrasnodar@yandex.ru', 'admin1234')
