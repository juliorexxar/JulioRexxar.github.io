from .models import Clase, Servicio ,Transaccion
from rest_framework import viewsets, permissions
from .serializers import ClaseSerializer, ServicioSerializer, TransaccionSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClaseSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicioSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransaccionSerializer
