# mysite/sitemaps.py
from django.contrib.sitemaps import Sitemap
from blog.models import Post
from products.models import Product, Category
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home'] 

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_updated


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all()


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated