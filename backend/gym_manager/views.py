from django.shortcuts import render
from .models import empleado, cliente, maquina, producto
from .serializer import EmpleadoSerializer, ClienteSerializer, MaquinaSerializer, ProductoSerializer
from rest_framework import viewsets

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = EmpleadoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer


class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = maquina.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer 