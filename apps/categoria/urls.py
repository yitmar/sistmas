from django.urls import include, path

from .views import inicio, categorias, nueva_categoria

urlpatterns=[
    path('', inicio.as_view(), name="categoria"),
    path(r'categorias', categorias.as_view(), name="categorias"),
    path(r'nueva_categoria', nueva_categoria.as_view(), name="nueva_categoria"),
    path(r'buscar_categoria', nueva_categoria.as_view(), name="buscar_categoria"),
    path(r'eliminar_categoria', categorias.as_view(), name="eliminar_categoria"),
]
