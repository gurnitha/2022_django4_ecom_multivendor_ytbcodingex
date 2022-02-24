# app/products/models.py

# Django modules
from django.db import models

# Create your models here.


# Class model:Slider
class Slider(models.Model):

	DISCOUNT_DEAL_CHOICES = (
		('HOT DEALS', 'Hot Deals'),
		('NEW ARRIVALS', 'New Arrivals'),
		('NEW DEALS', 'New Deals'),
	)

	image		= models.ImageField(upload_to='media/sliders')
	discount_deal	= models.CharField(choices=DISCOUNT_DEAL_CHOICES, max_length=100)
	sale		= models.IntegerField()
	brand_name	= models.CharField(max_length=100)
	discount	= models.IntegerField()
	link 		= models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Sliders'

	def __str__(self):
		return self.brand_name


# Class model:Features
class Features(models.Model):

	icon 		= models.CharField(max_length=100, blank=True)
	promo_title	= models.CharField(max_length=100, blank=True)
	promo_offer	= models.CharField(max_length=100, blank=True)

	class Meta:
		verbose_name_plural = 'Features'

	def __str__(self):
		return self.promo_title

# Class model:BannerTop
class BannerTop(models.Model):

	image 		= models.ImageField(upload_to='media/banners')
	promo_title	= models.CharField(max_length=100, blank=True)
	promo_subtitle	= models.CharField(max_length=100, blank=True)
	promo_offer	= models.CharField(max_length=100, blank=True)

	class Meta:
		verbose_name_plural = 'Banners top'

	def __str__(self):
		return self.promo_title


# Class model:BannerMiddle
class BannerMiddle(models.Model):

	image 		= models.ImageField(upload_to='media/banners')
	promo_title	= models.CharField(max_length=100, blank=True)
	promo_subtitle	= models.CharField(max_length=100, blank=True)
	promo_offer	= models.CharField(max_length=100, blank=True)

	class Meta:
		verbose_name_plural = 'Banners middle'

	def __str__(self):
		return self.promo_title


# Class model:BannerLower
class BannerLower(models.Model):

	BANNER_POSITION_CHOICES = (
		('TOP', 'Top'),
		('MIDDLE', 'Middle'),
		('LOWER', 'Lower'),
	)
	image 		= models.ImageField(upload_to='media/banners')
	promo_title	= models.CharField(max_length=100, blank=True)
	promo_subtitle	= models.CharField(max_length=100, blank=True)
	promo_offer	= models.CharField(max_length=100, blank=True)
	position    = models.CharField(choices=BANNER_POSITION_CHOICES, max_length=10, blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Banners lower'

	def __str__(self):
		return self.promo_title


# Class model:Brand
class Brand(models.Model):

	image 	= models.ImageField(upload_to='media/brands')
	name 	= models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Brands'

	def __str__(self):
		return self.name

