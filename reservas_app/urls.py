from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),

    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicios/crear/', views.servicio_create, name='servicio_create'),
    path('servicios/editar/<int:pk>/', views.servicio_update, name='servicio_update'),
    path('servicios/eliminar/<int:pk>/', views.servicio_delete, name='servicio_delete'),

    path('citas/', views.cita_list, name='cita_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/editar/<int:pk>/', views.cita_update, name='cita_update'),
    path('citas/eliminar/<int:pk>/', views.cita_delete, name='cita_delete'),
]
