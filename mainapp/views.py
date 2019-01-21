from django.shortcuts import render, get_object_or_404
from .models import Product, MenuCategory
from basketapp.models import Basket
import datetime


def main(request):
    new_products = Product.objects.all()[:3]
    top_products = Product.objects.all()[:3]
    sale_products = Product.objects.all()[:3]
    menu_categories = MenuCategory.objects.all()
    content = {'new_products': new_products,
               'top_products': top_products,
               'sale_products': sale_products,
               'menu_categories': menu_categories,
               'basket': getBasket(request.user)
               }
    return render(request, 'mainapp/index.html', content)


def apparel(request):
    return render(request, 'mainapp/apparel.html')


def page_not_found(request):
    return render(request, 'mainapp/404.html')


def checkout(request):
    return render(request, 'mainapp/checkout.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def login(request):
    return render(request, 'mainapp/login.html')


def register(request):
    return render(request, 'mainapp/register.html')


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    menu_categories = MenuCategory.objects.all()

    content = {
                'product': product,
                'menu_categories': menu_categories,
                'basket': getBasket(request.user)
               }

    return render(request, 'mainapp/product.html', content)


def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []
