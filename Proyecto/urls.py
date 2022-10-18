from django.contrib import admin
from django.urls import path
from MVT import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.index),
    path("mostrar_animales/", views.mostrarAnimal),
    path("estatico/", views.crear_statico),
]
