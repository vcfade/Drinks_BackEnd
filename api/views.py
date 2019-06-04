from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
import json
from api.models import Clientes, Bares, Bartenders, Productos, Ordenes, Detalle_De_Orden, Promociones, User, Roles
from .serializer import ClientesSerializer, BaresSerializer, BartendersSerializer, ProductosSerializer, OrdenesSerializer, Detalle_De_OrdenSerializer, PromocionesSerializer, UserSerializer

"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


class LoginAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'id': user.id,
            'role_id':user.role_id,
        })

class RegisterCliente(APIView):
    def post(self, request):
        data = request.data
        data['role'] = 1
        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            #newUser = User.objects.create_user(serializer.save()) \
            return Response(serializer.data)    
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterBartender(APIView):
    def post(self, request):
        data = request.data
        data['role'] = 2
        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            #newUser = User.objects.create_user(serializer.save()) \
            return Response(serializer.data)    
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAdmin(APIView):
    def post(self, request):
        data = request.data
        data['role'] = 3
        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            #newUser = User.objects.create_user(serializer.save()) \
            return Response(serializer.data)    
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def get(self, request, format= None):
        request.user.auth_token.delete()
        return Response ({"detail": "Log Out"}, status=status.HTTP_200_OK )

#################################>>>CLIENTES<<<###############################

class ClientView(APIView):
    def get(self, request, cliente_id=None):

        user = UserSerializer(User.objects.all(),many = True)
        print (user)
        if cliente_id is not None:
            cliente = Clientes.objects.get(id=cliente_id)
            serializer = ClientesSerializer(cliente, many=False)
            return Response(serializer.data)
        else:
            clientes = Clientes.objects.all()
            serializer = ClientesSerializer(clientes, many=True)
            return Response(serializer.data)

    def delete(self, request, cliente_id):

        cliente = Clientes.objects.get(id=cliente_id)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#################################### FALTA AGREGAR PUT METHOD PARA ACTUALIZAR CLIENTE

#################################>>>BARES<<<###############################

class BaresView(APIView):
    def get(self, request, bar_id=None):

        if bar_id is not None:
            bar = Bares.objects.get(id=bar_id)
            serializer = BaresSerializer(bar, many=False)
            return Response(serializer.data)
        else:
            bar = Bares.objects.all()
            serializer = BaresSerializer(bar, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = BaresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, bar_id):

        bar = Bares.objects.get(id=bar_id)
        bar.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

#################################>>>BARTENDER<<<###############################

class BartendersView(APIView):
    def get(self, request, bartender_id=None):

        if bartender_id is not None:
            bartender = Bartenders.objects.get(id=bartender_id)
            serializer = BartendersSerializer(bartender, many=False)
            return Response(serializer.data)
        else:
            bartender = Bartenders.objects.all()
            serializer = BartendersSerializer(bartender, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = BartendersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, bartender_id):

        bartender = Bartenders.objects.get(id=bartender_id)
        bartender.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
#############################>>>PRODUCTOS<<<###################################

class ProductosView(APIView):
    def get(self, request, producto_id=None):

        if producto_id is not None:
            producto = Productos.objects.get(id=producto_id)
            serializer = ProductosSerializer(producto, many=False)
            return Response(serializer.data)
        else:
            producto = Productos.objects.all()
            serializer = ProductosSerializer(producto, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, producto_id):

        producto = Productos.objects.get(id=producto_id)
        producto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

       
#################################>>>ORDENES<<<###############################

class OrdenesView(APIView):
    def get(self, request, orden_id=None):

        if orden_id is not None:
            orden = Ordenes.objects.get(id=orden_id)
            serializer = OrdenesSerializer(orden, many=False)
            return Response(serializer.data)
        else:
            orden = Ordenes.objects.all()
            serializer = OrdenesSerializer(orden, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = OrdenesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, orden_id):

        orden = Ordenes.objects.get(id=orden_id)
        orden.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

#################################>>>Detalle_De_Orden<<<###############################

class DetallesView(APIView):
    def get(self, request, detalle_id=None):

        if detalle_id is not None:
            detalle = Detalle_De_Orden.objects.get(id=detalle_id)
            serializer = Detalle_De_OrdenSerializer(detalle, many=False)
            return Response(serializer.data)
        else:
            detalle = Detalle_De_Orden.objects.all()
            serializer = Detalle_De_OrdenSerializer(detalle, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = Detalle_De_OrdenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, detalle_id):

        detalle = Detalle_De_Orden.objects.get(id=detalle_id)
        detalle.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

#################################>>>Promociones<<<###############################

class PromocionesView(APIView):
    def get(self, request, promocion_id=None):

        if promocion_id is not None:
            promocion = Promociones.objects.get(id=promocion_id)
            serializer = PromocionesSerializer(promocion, many=False)
            return Response(serializer.data)
        else:
            promocion = Promociones.objects.all()
            serializer = PromocionesSerializer(promocion, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = PromocionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, promocion_id):

        promocion = Promociones.objects.get(id=promocion_id)
        promocion.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
