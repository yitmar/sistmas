from django.urls import include, path

from .views import inicio, vistas_categorias, nueva_categoria, vista_eliminar_categoria

urlpatterns=[
    path('', inicio.as_view(), name="categoria"),
    path(r'categorias', vistas_categorias.as_view(), name="categorias"),
    path(r'nueva_categoria', nueva_categoria.as_view(), name="nueva_categoria"),
    path(r'buscar_categoria', nueva_categoria.as_view(), name="buscar_categoria"),
    path(r'^eliminar_categoria/(?P<pk>[0-9])\d/$', vista_eliminar_categoria, name="eliminar_categoria"),
]
