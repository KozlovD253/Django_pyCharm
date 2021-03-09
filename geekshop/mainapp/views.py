from django.shortcuts import render
import os
from django.conf import settings
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    title = 'Продукты'
    same_products =Product.objects.all()[:4]
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'Товары',
        'links_menu' : links_menu
    }

    return render(request, 'mainapp/products.html', content)

def contact(request):
    content = {
        'title': 'Контакты'
    }

    return render(request, 'mainapp/contact.html', content)
