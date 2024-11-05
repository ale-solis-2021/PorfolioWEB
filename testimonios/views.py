from django.shortcuts import render, redirect
from .models import Testimonio
from .forms import TestimonioForm

def lista_testimonios(request):
    testimonios = Testimonio.objects.all()  # Obtiene todos los testimonios
    if request.method == 'POST':
        form = TestimonioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_testimonios')
    else:
        form = TestimonioForm()
    return render(request, 'testimonios/lista_testimonios.html', {'testimonios': testimonios, 'form': form})

