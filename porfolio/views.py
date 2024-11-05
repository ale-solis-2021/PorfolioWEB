from django.shortcuts import render
from .models import project  # Modelo de proyectos
from testimonios.models import Testimonio  # Importa el modelo de Testimonio
from sobre_mi.models import SobreMi  # Importa el modelo de "Sobre mí"

def home(request):
    proyectos = project.objects.all()  # Obtén todos los proyectos
    sobre = SobreMi.objects.first()  # Obtén la primera instancia de "Sobre mí"
    testimonios = Testimonio.objects.all()  # Obtén todos los testimonios
    return render(request, 'home.html', {
        'proyectos': proyectos,
        'sobre': sobre,
        'testimonios': testimonios,
    })