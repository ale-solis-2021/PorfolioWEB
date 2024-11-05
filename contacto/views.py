from django.shortcuts import render, redirect
from .models import Contacto

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        # Guardar el mensaje en la base de datos
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        
        # Redirigir a la misma página después de enviar el mensaje
        return redirect('contacto')
    
    # Renderizar el template de contacto
    return render(request, 'contacto/contacto.html')


