from django.shortcuts import render
from django.http import HttpResponse
from .models import sub
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
 ListView,
 DetailView,
 CreateView,
 UpdateView,
 DeleteView,
 )

def support_us(request):
	return render(request ,'main/support_us.html')

# Create your views here.
def home(request):
	return render(request, "main/home.html")


def about(request):
	return HttpResponse('<h1>about')


@login_required
def dash_board(request):
    ordering = ['-date_end']
    subs = sub.objects.filter(author=request.user)
    
    context = {
        'subs': subs,
    }
    return render(request, "main/dash-board.html", context)

class SubListView(LoginRequiredMixin, ListView):#problem with the filter!
	model = sub
	template_name = "main/dash-board.html"
	context_object_name = 'subs'
	ordering = ['-date_end']

class SubDetailView(LoginRequiredMixin,UserPassesTestMixin ,DetailView):
	model = sub
	def test_func(self):
		sub = self.get_object()
		if self.request.user == sub.author:
			return True
		return False	




class SubCreateView(LoginRequiredMixin, CreateView):
	model = sub
	fields = ['provider', 'tier', 'price','date_started', 'date_end']
	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class SubUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
	model = sub
	fields = ['provider', 'tier', 'date_started', 'date_end']
	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	def test_func(self):
		sub = self.get_object()
		if self.request.user == sub.author:
			return True
		return False
		
class SubDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
	model = sub
	success_url = '/'
	def test_func(self):
		sub = self.get_object()
		if self.request.user == sub.author:
			return True
		return False