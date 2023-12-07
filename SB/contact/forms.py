from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import contact



class contact(forms.ModelForm):

	email = forms.EmailField()

	class Meta:
		model = contact
		fields = ['first_name', 'last_name', 'email', 'title', 'description']