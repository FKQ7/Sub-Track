from django.shortcuts import render
from django.http import HttpResponse
from .models import sub
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request, "main/home.html")


def about(request):
	return HttpResponse('<h1>about')


@login_required
def dash_board(request):
	context = {
		'subs':sub.objects.filter(author=request.user) #the string is the name of the data
	}
	return render(request, "main/dash-board.html", context)