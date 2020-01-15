"""MamGlosWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="main-home"),
    path('about/', views.about, name="main-about"),
    # path('adopted/', views.adopted, name="main-adopted"),
    path('adopted/', views.AdoptedList.as_view(), name="main-adopted"),
    path('contact/', views.contact, name="main-contact"),
    path('forAdoption/', views.ForAdoptionList.as_view(), name="main-forAdoption"),
    path('news/', views.NewsList.as_view(), name="main-news"),
    path('partner/', views.partner, name="main-partner"),
    path('support/', views.support, name="main-support"),
    path('volo/', views.volo, name="main-volo"),
    path('foundlost/', views.FoundLostList.as_view(), name="main-foundlost"),

]
