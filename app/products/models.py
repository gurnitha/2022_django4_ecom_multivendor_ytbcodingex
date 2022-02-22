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

