from rest_framework import serializers
from .models import Clientes, Bares, Bartender, Productos, Ordenes, Detalle_De_Orden, Promociones


class ClientesSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Clientes
        fields = '__all__'

class BaresSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Bares
        fields = '__all__'
        
class BartenderSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Bartender
        fields = '__all__'
        
class ProductosSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = '__all__'

class OrdenesSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Ordenes
        fields = '__all__'
        
class Detalle_De_OrdenSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Detalle_De_Orden
        fields = '__all__'
        
class PromocionesSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Promociones
        fields = '__all__'
        
