from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('clientes/<int:cliente_id>', views.ClientView.as_view(), name='id-clientes'),
    path('clientes/', views.ClientView.as_view(), name='all-clientes'),
    path('bares/', views.BaresView.as_view(), name='all-bars'),
    path('bares/<int:bar_id>', views.BaresView.as_view(), name='all-bars'),
]
