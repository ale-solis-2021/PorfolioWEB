from django.shortcuts import render
from porfolio.models import project  # Importa el modelo de proyectos desde la aplicación `porfolio`

def lista_proyectos(request):
    proyectos = project.objects.all()  # Obtiene todos los proyectos de la base de datos
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})
