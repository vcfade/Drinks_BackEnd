"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models


# Create your models here.

class Clientes(models.Model):
    first_name = models.CharField(max_length=30, default = '')
    last_name = models.CharField(max_length=30, default = '')
    email = models.EmailField()
    state = models.BooleanField(default=True)



class Bares (models.Model):
    bar_name: models.CharField(max_length=30,default = '')



class Bartender (models.Model):
    first_name = models.CharField(max_length=30, default = '')
    last_name = models.CharField(max_length=30, default = '')
    bar_id = models.ForeignKey (Bares, on_delete=models.CASCADE)

class Productos (models.Model):
    producto_name = models.CharField (max_length = 30, default = '')
    estado_producto = models.BooleanField(default = True)

class Ordenes (models.Model):
    client_id = models.ForeignKey (Clientes, on_delete=models.CASCADE)
    product_id = models.ForeignKey (Productos, on_delete=models.CASCADE)
    date_order = models.DateField()

class Detalle_De_Orden (models.Model):
    date_detalleOrden = models.DateField()
    order_id = models.ForeignKey(Ordenes, on_delete=models.CASCADE)
    estado_DDO = models.BooleanField(default=True)


class Promociones (models.Model):
    product_id = models.ForeignKey (Productos,on_delete=models.CASCADE)
