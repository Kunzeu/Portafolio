from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    image = ImageField(upload_to='porta/images/')
    urls = URLField(blank=True)
