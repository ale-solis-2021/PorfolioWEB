from django.db import models

class SobreMi(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    imagen_perfil = models.ImageField(upload_to='sobre_mi/images/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre