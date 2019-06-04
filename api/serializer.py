from rest_framework import serializers

from .models import Clientes, Bares, Bartenders, Productos, Ordenes, Detalle_De_Orden, Promociones, User, Roles


class ClientesSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Clientes
        fields = '__all__'

class RolesSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Roles
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
   #role = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
   #role = RolesSerializer(many=False)  
   class Meta:
       model = User
       fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role' )
       write_only_fields = ('password',)
       read_only_fields = ('id',)
       #depth = 1

   def create(self, validated_data):
       user = User.objects.create(
           username=validated_data['username'],
           email=validated_data['email'],
           first_name=validated_data['first_name'],
           last_name=validated_data['last_name'],
           role=validated_data['role']
       )

       user.set_password(validated_data['password'])
       user.save()

       return user

class BaresSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Bares
        fields = '__all__'
        
class BartendersSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Bartenders
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
        
