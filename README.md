# Session 4: Product Pages & SEO Implementation

## โครงสร้างที่จะสร้าง
```
products/
├── templates/products/
│   ├── product_list.html      # หน้าแสดงสินค้าทั้งหมด
│   ├── product_detail.html    # หน้าแสดงรายละเอียดสินค้า
│   ├── category_list.html     # หน้าแสดงหมวดหมู่ทั้งหมด
│   └── category_detail.html   # หน้าแสดงสินค้าในหมวดหมู่
└── models.py                  # โมเดลสินค้าและหมวดหมู่
```

## Models
```python
# products/models.py
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})
```

## Views
```python
# products/views.py
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {
        'product': product
    })

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {
        'categories': categories
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(available=True)
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })
```

## URLs
```python
# products/urls.py
from django.urls import path
from . import product_list, category_list, category_detail, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
```

## Sitemap Implementation
```python
# mysite/sitemaps.py
from django.contrib.sitemaps import Sitemap
from products.models import Product, Category

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all()
```

## SEO Optimization
1. Product Detail Page:
```html
{% block meta %}
<title>{{ product.name }} - SCFS</title>
<meta name="description" content="{{ product.description|truncatewords:25 }}">
<link rel="canonical" href="{{ request.build_absolute_uri }}">

<!-- Open Graph Tags -->
<meta property="og:title" content="{{ product.name }}">
<meta property="og:description" content="{{ product.description|truncatewords:25 }}">
<meta property="og:image" content="{{ product.image.url }}">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
{% endblock %}
```

2. Category Detail Page:
```html
{% block meta %}
<title>{{ category.name }} - SCFS</title>
<meta name="description" content="{{ category.description }}">
<link rel="canonical" href="{{ request.build_absolute_uri }}">
{% endblock %}
```

## Templates Structure
1. Product List (product_list.html)
   - Grid layout showing all products
   - Image, title, price, and description
   - Link to detail page

2. Product Detail (product_detail.html)
   - Full product information
   - Large product image
   - Price and stock status
   - Category link

3. Category List (category_list.html)
   - All product categories
   - Category description
   - Link to category detail

4. Category Detail (category_detail.html)
   - Products in specific category
   - Category description
   - Products in grid layout

## Additional Features
1. รองรับ SEO
   - Meta tags
   - Canonical URLs
   - Sitemap.xml

2. การจัดการรูปภาพ
   - Upload to media folder
   - Proper alt tags
   - Responsive images

3. URLs
   - SEO-friendly slugs
   - Proper hierarchy
   - Clean URLs

4. Breadcrumbs
   - Home > Category > Product
   - Proper navigation structure


