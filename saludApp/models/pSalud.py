from django.db import models
from .usuario import Usuario

class PersonalSalud(models.Model):
    documento = models.CharField(primary_key=True, max_length = 10, unique=True)
    rol = models.CharField('Rol', max_length = 100)
    especialidad = models.CharField('Especialidad', max_length = 100)
    username = models.OneToOneField(Usuario, related_name='pSalud', on_delete=models.CASCADE)