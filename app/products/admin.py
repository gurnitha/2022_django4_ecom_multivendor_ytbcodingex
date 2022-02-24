# app/products/models.py

# Django modules
from django.contrib import admin

# Locals
from app.products.models import (
	Slider, Features, BannerTop, 
	BannerMiddle, BannerLower, Brand)


# Register your models here.
admin.site.register(Slider)
admin.site.register(Features)
admin.site.register(BannerTop)
admin.site.register(BannerMiddle)
admin.site.register(BannerLower)
admin.site.register(Brand)