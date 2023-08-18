"""DjangoCountries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from MainApp import views

urlpatterns = [
	path('', views.home),
    path('country/<str:name>', views.get_country, name = "get_country"),
    path('language/<str:name>', views.get_language, name = "get_language"),
    path('countries-list/', views.get_countries_list, name = "get_countries_list"),
    path('languages-list/', views.get_languages_list, name = "get_languages_list"),
]




