"""
URL configuration for SB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import SubListView, SubDetailView, SubCreateView, SubUpdateView, SubDeleteView
urlpatterns = [
    path('', views.home, name="home"),
    path('support-us/', views.support_us, name="support_us"),
    path('about/', views.about, name="about"),
    path('dash-board/', views.dash_board, name='dash-board'),
    path('sub/<pk>/', SubDetailView.as_view(), name='sub-detail'),
    path('sub-create/new/', SubCreateView.as_view(), name='sub-Create'),
    path('sub/<pk>/update', SubUpdateView.as_view(), name='sub-update'),
    path('sub/<pk>/delete', SubDeleteView.as_view(), name='sub-delete'),

]
