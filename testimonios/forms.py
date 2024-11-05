from django import forms
from .models import Testimonio

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['nombre', 'testimonio', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'testimonio': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
