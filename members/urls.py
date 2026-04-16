from django.urls import path, include
from django.contrib import admin
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(),name = 'register'),   
]

