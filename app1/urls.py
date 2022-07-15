from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('weather/',views.weather, name="weather"),
    path('bitcoin/',views.bitcoin, name="bitcoin"),
]