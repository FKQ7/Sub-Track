from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg' ,upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'
#resizing img is missing 