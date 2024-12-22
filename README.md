# Session 2: Django Models, Views และ Templates

## โครงสร้างการทำงาน
```
mysite/                # โปรเจคหลัก 
├── blog/              # แอปพลิเคชัน blog
│   ├── models.py      # กำหนดโครงสร้างฐานข้อมูล
│   ├── views.py       # ลอจิคการทำงาน
│   ├── urls.py        # กำหนด URL patterns
│   ├── admin.py       # Register models ใน admin
│   └── templates/     # โฟลเดอร์เก็บไฟล์ HTML
│       └── blog/
│           └── home.html
└── mysite/            # ตัวเว็บไซต์หลัก
    ├── settings.py    # ตั้งค่าโปรเจค
    └── urls.py        # URL หลักของเว็บไซต์
```

## 1. การสร้าง Model
ใน `blog/models.py`:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
```

## 2. ลงทะเบียน Model ใน Admin
ใน `blog/admin.py`:
```python
from django.contrib import admin 
from .models import Post 

admin.site.register(Post)
```

## 3. สร้าง View
ใน `blog/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')
```

## 4. กำหนด URLs
ใน `blog/urls.py`:
```python
from django.urls import path 
from .views import home 

urlpatterns = [
    path('', home),
]
```

ใน `mysite/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
```

## 5. ลงทะเบียน App
ใน `mysite/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'  # เพิ่ม app blog
]
```

## 6. สร้าง Template
สร้างไฟล์ `blog/templates/blog/home.html`:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Sonny shopping web</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <!-- Navbar และ Content -->
        <div class="container">
            <h1>Welcome to the Blog</h1>
            <!-- เนื้อหาเว็บไซต์ -->
        </div>
    </body>
</html>
```

## ขั้นตอนการรันโปรเจค

1. อัพเดทฐานข้อมูล:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. รันเซิร์ฟเวอร์:
```bash
python manage.py runserver
```

3. เข้าใช้งานเว็บไซต์:
- หน้าหลัก: http://127.0.0.1:8000/
- หน้า Admin: http://127.0.0.1:8000/admin

## โครงสร้างข้อมูล Post
- title: ชื่อบทความ (ความยาวไม่เกิน 100 ตัวอักษร)
- description: คำอธิบายสั้นๆ (ความยาวไม่เกิน 200 ตัวอักษร)
- body: เนื้อหาบทความ
- date_created: วันที่สร้าง (บันทึกอัตโนมัติ)
- date_updated: วันที่อัพเดท (อัพเดทอัตโนมัติ)