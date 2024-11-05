from django.db import models
from django.db.models.fields import CharField, URLField
# para imagenes
from django.db.models.fields.files import ImageField

# guardar los datos de mi portafolio
class project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=300)
    image =ImageField(upload_to='porfolio/images/')
    url = URLField(blank=True)
