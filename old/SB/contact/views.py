from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import contact
# Create your views here.
def contact_us(request):
	if request.method == "POST":
		form = contact(request.POST)
		if form.is_valid():
			form.save()
			return(redirect('home'))
	else:
		form = contact()
	return render(request ,'contact/contact_us.html', {"form":form})