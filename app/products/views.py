# app/products/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.products.models import (
	Slider, Features, BannerTop, 
	BannerMiddle, BannerLower, Brand)

# Create your views here.


# Views: product_list
def product_list(request):

	slider_list = Slider.objects.all()
	features = Features.objects.all()
	banner_top  = BannerTop.objects.all()
	banner_middle = BannerMiddle.objects.all()
	banner_lower_top  = BannerLower.objects.order_by('id')[0:1]
	banner_lower_middle  = BannerLower.objects.order_by('id')[1:3]
	banner_lower_lower  = BannerLower.objects.order_by('id')[3:4]
	brands = Brand.objects.all()
	context = {
		'slider_list':slider_list,
		'features':features,
		'slider_list':slider_list,
		'banner_top':banner_top,
		'banner_middle':banner_middle,
		'banner_lower_top':banner_lower_top,
		'banner_lower_middle':banner_lower_middle,
		'banner_lower_lower':banner_lower_lower,
		'brands':brands,
	}
	
	return render(request, 'products/index.html', context)