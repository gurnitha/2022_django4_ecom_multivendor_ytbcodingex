# app/products/views.py

# Django modules
from django.shortcuts import render

# Create your views here.


# Views: product_list
def product_list(request):
	return render(request, 'products/index.html')