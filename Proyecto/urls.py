from django.contrib import admin
from django.urls import path
from MVT import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.index),
    path("mostrar_animales/", views.mostrarAnimal),
    path("estatico/", views.crear_statico),
    path("segundo_estatico", views.segundo_estatico),
    path("buscar/", views.BuscarAnimal.as_view()),
    path("mi-animal/alta", views.AltaAnimal.as_view()),
    path("empleado/alta", views.AltaEmpleado.as_view()),
    path("cliente/alta", views.AltaCliente.as_view()),
]
