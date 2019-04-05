from django.shortcuts import render, get_object_or_404
from .models import Product, MenuCategory


def main(request):
    new_products = Product.objects.all()[:3]
    top_products = Product.objects.all()[:3]
    sale_products = Product.objects.all()[:3]
    menu_categories = MenuCategory.objects.all()
    content = {'new_products': new_products,
               'top_products': top_products,
               'sale_products': sale_products,
               'menu_categories': menu_categories,
               }
    return render(request, 'mainapp/index.html', content)


def apparel(request):
    menu_categories = MenuCategory.objects.all()
    apparel_products = Product.objects.all().filter(menu_category=8)
    content = {'apparel_products': apparel_products,
               'menu_categories': menu_categories,
               }
    return render(request, 'mainapp/apparel.html', content)


def page_not_found(request):
    return render(request, 'mainapp/404.html')


def checkout(request):
    return render(request, 'mainapp/checkout.html')


def contact(request):
    menu_categories = MenuCategory.objects.all()
    content = {'menu_categories': menu_categories,
               }
    return render(request, 'mainapp/contact.html', content)


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
    }

    return render(request, 'mainapp/product.html', content)
