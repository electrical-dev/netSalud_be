from django.db import models
from .paciente import Paciente

class SignoVital(models.Model):
    idSignoVital = models.AutoField(primary_key=True)
    oximetria = models.CharField('Oximetria', max_length = 100)
    frec_respiratoria = models.CharField('Frecuencia Respiratoria', max_length = 100)
    frec_cardiaca = models.CharField('Frecuencia Cardiaca', max_length = 100)
    temperatura = models.CharField('Temperatura', max_length = 100)
    glicemias = models.CharField('Glicemias', max_length = 100)
    presion_arterial = models.CharField('Presion Arterial', max_length = 100)
    fecha_hora = models.DateTimeField('Fecha y Hora')
    paciente_documento = models.ForeignKey(Paciente, related_name='signoVital', on_delete=models.CASCADE)