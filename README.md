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
=======
# Session 1: เริ่มต้นเรียนรู้ Django Framework

## โครงสร้างโปรเจค
```
myshop/                  # โฟลเดอร์หลักของโปรเจค
├── env/                 # Virtual Environment
├── mysite/             # ตัวเว็บไซต์หลัก
├── blog/               # แอพพลิเคชั่น blog
└── db.sqlite3          # ฐานข้อมูล
```

## ขั้นตอนการติดตั้งและรัน Project

### 1. สร้าง Virtual Environment
```bash
# สร้างโฟลเดอร์เพื่อเก็บโปรเจคท์
mkdir myshop
cd myshop

# สร้าง virtual environment
python -m venv env

# เปิดใช้งาน virtual environment
# สำหรับ Windows
env\Scripts\activate

# สำหรับ Mac/Linux
source env/bin/activate
```

### 2. ติดตั้ง Django
```bash
pip install django
```

### 3. สร้างโปรเจค Django
```bash
django-admin startproject mysite
```

### 4. สร้าง App
```bash
python manage.py startapp blog
```

### 5. ตั้งค่าฐานข้อมูล
```bash
# สร้างไฟล์การอัพเดทฐานข้อมูล
python manage.py makemigrations

# อัพเดทฐานข้อมูล
python manage.py migrate
```

### 6. สร้าง Superuser (ผู้ดูแลระบบ)
```bash
python manage.py createsuperuser
# ใส่ username
# ใส่ email (หรือกด Enter เพื่อข้าม)
# ใส่ password (password จะไม่โชว์ในหน้านี้)
# ยืนยัน password
```

### 7. รันเซิร์ฟเวอร์
```bash
python manage.py runserver
```

## การเข้าใช้งาน

1. หน้าเว็บไซต์หลัก: http://127.0.0.1:8000/
   - จะเห็นหน้า Welcome to Django

   <img src="https://drive.google.com/uc?export=view&id=1octX1nGpWDM7f0B-qnP-LMdivX9BYETO" alt="Django Welcome Page" width="600"/>

2. หน้า Admin: http://127.0.0.1:8000/admin
   - เข้าสู่ระบบด้วย superuser ที่สร้างไว้

   <img src="https://drive.google.com/uc?export=view&id=1pvaIfz9N1N9P7FlZdsdi2SJTBik__k-f" alt="Django Admin Login" width="600"/>

## หมายเหตุสำคัญ
- ต้องเปิด virtual environment ทุกครั้งก่อนรันโปรเจค
- ถ้าเจอ error ให้ตรวจสอบว่าได้รัน migrate แล้วหรือยัง
- ไฟล์ `db.sqlite3` จะถูกสร้างหลังจากรัน migrate ครั้งแรก

## คำสั่งที่ใช้บ่อย
```bash
# เปิด virtual environment
source env/bin/activate  # (Mac/Linux)
env\Scripts\activate    # (Windows)

# รันเซิร์ฟเวอร์
python manage.py runserver

# ปิด virtual environment
deactivate
```

## การแก้ปัญหาเบื้องต้น

1. ถ้ารันเซิร์ฟเวอร์ไม่ได้:
   - ตรวจสอบว่าเปิด virtual environment แล้ว
   - ตรวจสอบว่าอยู่ในโฟลเดอร์ที่มีไฟล์ manage.py

2. ถ้าเข้า admin ไม่ได้:
   - ตรวจสอบว่ารัน migrate แล้ว
   - ตรวจสอบว่าสร้าง superuser แล้ว

3. ถ้าลืม password superuser:
   ```bash
   python manage.py changepassword username
   ```
