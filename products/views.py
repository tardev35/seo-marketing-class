from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/product_detail.html', {'product': product})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(available=True)

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'products/category_detail.html', context)

# products/templates/products
