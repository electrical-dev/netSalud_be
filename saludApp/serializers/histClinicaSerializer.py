from saludApp.models.historiaClinica import HistoriaClinica
from rest_framework import serializers

class HistClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['sugerencias', 'diagnostico', 'entorno', 'fecha_sug', 'descripcion', 'paciente_documento']