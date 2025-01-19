from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post 
from products.models import Product, Category


def home(request):
    all_posts = Post.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'all_posts': all_posts,
        'products': products,
        'categories': categories
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, post_id):
    single_post = get_object_or_404(Post, id=post_id)

    context = {
        'single_post': single_post
    }

    return render(request, 'blog/post_detail.html', context)




