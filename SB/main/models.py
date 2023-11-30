from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class sub(models.Model):
	provider = models.CharField(max_length=70)
	tier = models.CharField(max_length=40)
	date_started = models.DateField(auto_now=False, auto_now_add=False)
	date_end = models.DateField(auto_now=False, auto_now_add=False, )
	author = models.ForeignKey(User, on_delete=models.CASCADE)
