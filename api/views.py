from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Clientes, Bares, Bartender, Productos, Ordenes, Detalle_De_Orden, Promociones
from .serializer import ClientesSerializer, BaresSerializer, BartenderSerializer, ProductosSerializer, OrdenesSerializer, Detalle_De_OrdenSerializer, PromocionesSerializer

"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""
class ClientView(APIView):
    def get(self, request, cliente_id=None):

        if cliente_id is not None:
            cliente = Clientes.objects.get(id=cliente_id)
            serializer = ClientesSerializer(cliente, many=False)
            return Response(serializer.data)
        else:
            clientes = Clientes.objects.all()
            serializer = ClientesSerializer(clientes, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, cliente_id):

        cliente = Clientes.objects.get(id=cliente_id)
        cliente.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

#################################### FALTA AGREGAR PUT METHOD PARA ACTUALIZAR CLIENTE

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
