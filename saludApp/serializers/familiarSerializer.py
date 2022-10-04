from saludApp.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['documento', 'parentesco', 'correo', 'username', 'paciente_documento']