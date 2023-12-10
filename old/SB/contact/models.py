from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class contact(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	def __str__(self):
		return f'title: {self.title}'	