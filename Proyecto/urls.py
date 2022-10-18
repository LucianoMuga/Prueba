from django.contrib import admin
from django.urls import path
from MVT.views import index, mostrarAnimal

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", index),
    path("mostrar_animales/", mostrarAnimal)
]
