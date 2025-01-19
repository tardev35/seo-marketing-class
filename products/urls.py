from django.urls import path
from .views import product_list, product_detail, category_detail


urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]