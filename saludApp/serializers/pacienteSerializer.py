from saludApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['documento', 'fecha_nac', 'ciudad', 'direccion', 'pSalud_documento', 'username',]