from saludApp.models.pSalud import PersonalSalud
from rest_framework import serializers

class PSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSalud
        fields = ['documento', 'rol', 'especialidad', 'username']