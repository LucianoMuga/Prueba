from django.urls import path
from panel_app.views import AnimalList, AnimalBorrar, AnimalActualizar, AnimalCrear

urlpatterns = [
    path("", AnimalList.as_view(), name ="panel-list"),
    path("crear", AnimalCrear.as_view(), name ="panel-crear"),
    path('<int:pk>/borrar', AnimalBorrar.as_view(), name ="animal-borrar"),
    path('<int:pk>/actualizar', AnimalActualizar.as_view(), name ="animal-actualizar"),
]