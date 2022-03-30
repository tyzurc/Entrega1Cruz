from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    contenido = models.CharField(max_length=200)
    autorx = models.CharField(max_length=60, default="Nombre")
    fecha_creacion = models.DateField(default=datetime.now)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    user_name = models.CharField(max_length=60, default="User")
    email = models.CharField(max_length=60)
    # ver después cómo agregar cant. de posts hechos por cada user