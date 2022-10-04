from django.db import models
from .paciente import Paciente

class HistoriaClinica(models.Model):
    id_historia_cl = models.AutoField(primary_key=True)
    sugerencias = models.CharField('Sugerencias', max_length = 500)
    diagnostico = models.CharField('Diagnostico', max_length = 500)
    entorno = models.CharField('Entorno', max_length = 500)
    fecha_sug = models.DateField('Fecha Sugerencia')
    descripcion = models.CharField('Descripción', max_length = 500)
    paciente_documento = models.ForeignKey(Paciente, related_name='historiaClinica', on_delete=models.CASCADE)