from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('clientes/<int:cliente_id>', views.ClientView.as_view(), name='id-clientes'),
    path('clientes/', views.ClientView.as_view(), name='all-clientes'),

    path('bares/', views.BaresView.as_view(), name='id-bars'),
    path('bares/<int:bar_id>', views.BaresView.as_view(), name='all-bars'),
    
    path('bartenders/', views.BartendersView.as_view(), name='all-bartenders'),
    path('bartenders/<int:bartender_id>', views.BartendersView.as_view(), name='id-bartenders'),

    path('productos/', views.ProductosView.as_view(), name='all-productos'),
    path('productos/<int:productos_id>', views.ProductosView.as_view(), name='id-productos'),

    path('ordenes/', views.OrdenesView.as_view(), name='all-ordenes'),
    path('ordenes/<int:orden_id>', views.OrdenesView.as_view(), name='id-ordenes'),

    path('detalles/', views.DetallesView.as_view(), name='all-detalles'),
    path('detalles/<int:detalle_id>', views.DetallesView.as_view(), name='id-detalle'),

    path('promociones/', views.PromocionesView.as_view(), name='all-promociones'),
    path('promociones/<int:promocion_id>', views.PromocionesView.as_view(), name='id-promocion'),
]
