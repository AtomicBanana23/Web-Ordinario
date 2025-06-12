from rest_framework import serializers
from .models import empleado, cliente, maquina, producto

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquina
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'