from django.db import models
from django.db.models import Q
import random
import os
from django.db.models import Manager
from django.urls import reverse

# Create your models here.
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name , ext = os.path.splitext(base_name)
	return name , ext

def upload_img_path(instance,filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1,2000)
	name , ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return 'products/{new_filename}/{final_filename}'.format(
		new_filename=new_filename,
		final_filename=final_filename)


class ProductManager(models.Manager):
	def featured(self):
		return self.get_queryset().filter(featured=True)

	def get_by_id(self,id):
		qs = self.get_queryset().filter(id=id)
		if qs.count()==1:
			return qs.first()

		return None

	def search(self,query):
		lookups=Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
		return self.get_queryset().filter(lookups).distinct()

	

class Product(models.Model): #product category
	title = models.CharField(max_length=120)
	slug = models.SlugField(blank=True,unique=True)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2,max_digits=20, default=39.99)
	image = models.ImageField(upload_to=upload_img_path,null=True,blank=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	objects = ProductManager()

	def get_absolute_url(self):
		#return '/product/{slug}/'.format(slug=self.slug)
		return reverse('slug detail',kwargs={'slug':self.slug})

	def __str__(self):
		return self.title

