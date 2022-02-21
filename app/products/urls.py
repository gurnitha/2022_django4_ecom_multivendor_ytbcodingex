# app/products/urls.py

# Django modules
from django.urls import path

# Locals
from app.products import views

# App name
app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='index'),
]
