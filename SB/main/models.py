from django.db import models
from django.contrib.auth.models import User
import uuid 
from django.urls import reverse
from datetime import date
# Create your models here.
class sub(models.Model):
	id = models.UUIDField(default=uuid.uuid4, primary_key = True, editable = False)
	provider = models.CharField(max_length=70)
	tier = models.CharField(max_length=40)
	date_started = models.DateField(auto_now=False, auto_now_add=False)
	date_end = models.DateField(auto_now=False, auto_now_add=False, )
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	
	def remain(self):
		today = date.today()
		remaining_days = (self.date_end - today).days
		return(remaining_days)

	def get_absolute_url(self):
		return reverse('sub-detail', kwargs={'pk':self.id})