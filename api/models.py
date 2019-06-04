"""
All your application modules and serializers are going to be declared inside this file
"""
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

#Role managament System:
    # 1 = Client App 
    # 2 = Bartender
    # 3 = Admin


class Roles (models.Model):
    codeNAme = models.CharField(max_length=30,default = '') 
    name = models.CharField(max_length=30,default = '')  

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Roles,related_name='role', on_delete=models.CASCADE, null = True, blank = True)



class Bares (models.Model):
    bar_name = models.CharField(max_length=30,default = '')

class Administrador (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    bar_id = models.ForeignKey (Bares, on_delete=models.CASCADE)

class Clientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    state = models.BooleanField(default=True)
    @classmethod
    def create(cls, user):
        cliente = cls(user=user)
        # do something with the book
        return cliente

class Bartenders (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    bar_id = models.ForeignKey (Bares, on_delete=models.CASCADE)

class Productos (models.Model):
    producto_name = models.CharField (max_length = 30, default = '')
    estado_producto = models.BooleanField(default = True)


class Ordenes (models.Model):
    client_id = models.ForeignKey (Clientes, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True, blank=True)


class Detalle_De_Orden (models.Model):
    date_detalleOrden = models.DateTimeField(auto_now_add=True, blank=True)
    product_id = models.ForeignKey (Productos,default = 0, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Ordenes, on_delete=models.CASCADE)
    estado_DDO = models.BooleanField(default=True)


class Promociones (models.Model):
    product_id = models.ForeignKey (Productos,on_delete=models.CASCADE)
