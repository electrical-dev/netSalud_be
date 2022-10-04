from urllib import request
from rest_framework import generics,status, views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from saludApp.models import Paciente
from saludApp.serializers.pacienteSerializer import PacienteSerializer

class CrearPacienteView(views.APIView):
    def post(self,request):
        serializer=PacienteSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerPaciente(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def detalle(request, documento, *args, **kwargs):
        usuario = get_object_or_404(Paciente, pk=documento)

        return request
