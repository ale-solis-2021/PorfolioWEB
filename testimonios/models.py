from django.db import models

class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    testimonio = models.TextField()
    foto = models.ImageField(upload_to='testimonios/fotos/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.testimonio[:20]}..."

