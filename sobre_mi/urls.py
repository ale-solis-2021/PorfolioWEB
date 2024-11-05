from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre_mi, name='sobre_mi'),
]