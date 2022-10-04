from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class Familiar(models.Model):
    documento = models.CharField(primary_key=True, max_length = 10, unique=True)
    parentesco = models.CharField('Parentesco', max_length = 100)
    correo = models.EmailField('Correo', max_length = 100)
    username = models.OneToOneField(Usuario, related_name='familiar', on_delete=models.CASCADE)
    paciente_documento = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)