from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_testimonios, name='lista_testimonios'),
]