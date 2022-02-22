# app/products/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.products.models import Slider

# Create your views here.


# Views: product_list
def product_list(request):
	slider_list = Slider.objects.all()
	context = {'slider_list':slider_list}
	return render(request, 'products/index.html', context)