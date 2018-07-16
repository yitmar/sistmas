from django.urls import include, path, re_path
from .views import inicio, asignar_prueba, crear_prueba, lista_prueba, datos
#from .ajax import get_categorias, get_dificultad

urlpatterns=[
    path(r'', inicio.as_view(),name="pruebas"),
    path(r'^ver_prueba/(?P<pk>[0-9])\d/$', datos, name="ver_prueba"),
    path(r'asignar_prueba', asignar_prueba.as_view(), name="asignar_prueba"),
    path(r'crear_prueba', crear_prueba, name="crear_prueba"),
    path(r'lista_prueba', lista_prueba.as_view(),name="lista_prueba"),
#    path(r'^ajax/get_categorias/$', get_categorias, name='get_categorias'),
#    path(r'^ajax/get_dificultad/$', get_dificultad, name='get_dificultad'),
#    path('pruaba_pruebas', vista_ubicacion, name='pruebas_pruebas'),
#    path(r'prueba_prueba', vista_filtro_preguntas.as_view(), name="pruebas_pruebas" ),
#    path(r'prueba_prueba', search, name="pruebas_pruebas" ),
]

