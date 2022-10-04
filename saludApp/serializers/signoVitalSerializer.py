from saludApp.models.signoVital import SignoVital
from rest_framework import serializers

class SignoVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignoVital
        fields = ['oximetria', 'frec_respiratoria', 'frec_cardiaca', 'temperatura', 'glicemias', 'presion_arterial', 'fecha_hora', 'paciente_documento']