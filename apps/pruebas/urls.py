from django.urls import include, path, re_path
from .views import inicio, vista_crear_prueba, lista_prueba, vista_listar_pruebas, vista_ver_pruebas_asignadas, vista_buscar_preguntas, vista_eliminar_prueba, vista_Asignar_prueba, vista_realizar_prueba
#from .ajax import get_categorias, get_dificultad

urlpatterns=[
    path(r'', inicio.as_view(),name="pruebas"),
    path(r'listar_prueba/(<pk>[0-9])(<tipo>[0-9])',vista_listar_pruebas,name="listar_prueba"),
    path(r'crear_prueba/(<pk>[0-9])(<tipo>[0-9])', vista_crear_prueba, name="crear_prueba"),
    path(r'eliminar_prueba/<pk>[0-9])', vista_eliminar_prueba, name="eliminar_prueba"),
    
    path(r'asignar_prueba/', vista_Asignar_prueba , name="asignar_prueba"),

    path(r'buscar_preguntas/(<pk>[0-9])', vista_buscar_preguntas, name="buscar_preguntas"),
    path(r'lista_prueba/\d+', vista_ver_pruebas_asignadas, name="lista_prueba"),
    path(r'ver_prueba/(<pk>[0-9])', vista_realizar_prueba, name="ver_prueba"),

]