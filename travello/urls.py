# travello/urls.py
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index')]  # Example index view for the root URL