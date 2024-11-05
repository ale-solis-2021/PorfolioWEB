from django.shortcuts import render
from .models import SobreMi

def sobre_mi(request):
    sobre = SobreMi.objects.first()
    print("esto tengo en sobre mi",sobre)
    return render(request, 'sobre_mi/sobre_mi.html', {'sobre': sobre})

