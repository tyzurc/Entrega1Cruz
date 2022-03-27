from pickle import TRUE
from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=TRUE)
    titulo = models.CharField(max_length=60)
    contenido = models.TextField()