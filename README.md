# Session 3: Django Models, Views และการดึงข้อมูล

## โครงสร้างการทำงาน
```
mysite/
├── blog/
│   ├── models.py      # กำหนดโครงสร้างข้อมูล
│   ├── views.py       # ตรรกะการดึงข้อมูล
│   ├── urls.py        # กำหนด URL patterns
│   └── templates/     # โฟลเดอร์เก็บไฟล์ HTML
│       └── blog/           
│           ├── base.html (ไฟล์แม่ ใช้สืบทอด template)
│           ├── home.html
│           └── post_detail.html
└── media/            # โฟลเดอร์เก็บรูปภาพ
    └── blog_images/  # รูปภาพจาก featured_image
```

## 1. การดึงข้อมูลจากฐานข้อมูล (Blog List & Detail)

### โมเดล Post
```python
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    featured_image = models.ImageField(
        upload_to='blog_images/',
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
```

### Views สำหรับแสดงข้อมูล
```python
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    single_post = get_object_or_404(Post, id=post_id)
    context = {
        'single_post': single_post
    }
    return render(request, 'blog/post_detail.html', context)
```

### URLs Configuration
```python
# urls.py
from django.urls import path
from .views import home, post_detail

urlpatterns = [
    path('', home),
    path('blog/<int:post_id>/', post_detail)
]
```

## 2. การแสดงผลข้อมูลใน Template

### หน้าแรก (Home Page)
```html
{% extends 'blog/base.html' %}
{% block meta %}
<title>SCFS - จำหน่ายอาหารแมวทุกประเภท จัดส่งฟรีทั่วประเทศ</title>
{% endblock %}

{% block content %}
<div class="container">
    <!-- Hero Section -->
    <div class="bg-light text-dark py-5 mb-5">
        <!-- Hero content -->
    </div>

    <h2>Blog</h2>
    <div class="row">
        {% for post in all_posts %}
        <div class="col-sm-4">
            <div class="card">
                <div class="card-body">
                    <img src="{{ post.featured_image.url }}" 
                         class="card-img-top" 
                         alt="{{ post.title }}">
                    <h5 class="card-title">{{ post.title }}</h5>
                    <p class="card-text">{{ post.description }}</p>
                    <a href="/blog/{{ post.id }}" 
                       class="btn btn-primary">อ่านเพิ่มเติม</a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

### หน้ารายละเอียดบทความ (Post Detail)
```html
{% extends 'blog/base.html' %}
{% block meta %}
<title>{{ single_post.title }}</title>
<meta name="description" content="{{ single_post.description }}">
<link rel="canonical" href="{{ single_post.get_absolute_url }}">
{% endblock %}

{% block content %}
<div class="container">
    <div class="col-sm-8">
        <h1>{{ single_post.title }}</h1>
        <p>{{ single_post.description }}</p>
        <img src="{{ single_post.featured_image.url }}" 
             class="img-fluid" 
             alt="{{ single_post.title }}">
    </div>
</div>
{% endblock %}
```

## 3. การจัดการรูปภาพ (Image Upload)

### ตั้งค่าใน settings.py
```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### เพิ่ม URL patterns สำหรับไฟล์ media
```python
# urls.py (หลัก)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL patterns อื่นๆ
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 4. การเพิ่ม Meta Tags และ Social Share

### Facebook Open Graph
```html
<meta property="og:title" content="{{ single_post.title }}">
<meta property="og:description" content="{{ single_post.description }}">
<meta property="og:image" content="{{ single_post.featured_image.url }}">
<meta property="og:url" content="{{ request.build_absolute_uri }}">
```

### Twitter Cards
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ single_post.title }}">
<meta name="twitter:description" content="{{ single_post.description }}">
<meta name="twitter:image" content="{{ single_post.featured_image.url }}">
```

## การรันโปรเจค
1. ตรวจสอบว่าอยู่ใน virtual environment:
```bash
source env/bin/activate  # สำหรับ Mac/Linux
env\Scripts\activate    # สำหรับ Windows
```

2. รันเซิร์ฟเวอร์:
```bash
python manage.py runserver
```

## หมายเหตุ
- ต้องติดตั้ง Pillow สำหรับจัดการรูปภาพ: `pip install Pillow`
- ควรสร้างโฟลเดอร์ media/ ก่อนอัพโหลดรูปภาพ
- รูปภาพที่อัพโหลดควรมีขนาดที่เหมาะสมเพื่อประสิทธิภาพ
- ควรใส่ alt text ให้รูปภาพเสมอสำหรับ SEO