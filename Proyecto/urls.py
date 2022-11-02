from django.contrib import admin
from django.urls import path, include
from MVT import views
# from blog.views import index as blog_index

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
    path("panel-app/", include("panel_app.urls")),
    # path("blog/", blog_index),
    path("blog/", include("blog.urls")),
]
