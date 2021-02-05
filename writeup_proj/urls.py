"""writeup_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from writeapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    # HacktheBox Writeups
    path('querier/', views.querier, name='querier'),
    path('blackfield/', views.blackfield, name='blackfield'),
    path('feline/', views.feline, name='feline'),

    # OSCP Journey
    path('htbj/', views.htbj, name='htbj'),

    # Synack Challanges
    path('baby_international/', views.baby_international, name='baby_international'),
    path('babysql/', views.babysql, name='babysql'),
    path('passage/', views.passage, name='passage'),


]
