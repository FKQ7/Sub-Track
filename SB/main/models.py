from django.db import models
from django.contrib.auth.models import User
import uuid 
from django.urls import reverse
from datetime import date
# Create your models here.
class sub(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.CharField(max_length=70)
    tier = models.CharField(max_length=40)
    date_started = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    d_remain = models.IntegerField(default=0)  # New field to store days remaining

    def remain(self):
        today = date.today()
        remaining_days = (self.date_end - today).days
        self.d_remain = remaining_days  # Update d_remain with calculated value
        self.save()  # Save the updated model instance
        return remaining_days

    def get_absolute_url(self):
        return reverse('sub-detail', kwargs={'pk': self.id})