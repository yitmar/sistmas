from django.urls import include, path
from django.conf.urls import url
from .views import lista_categorias, vista_lista_preguntas, vista_crear_preguntas, vista_eliminar_pregunta, vista_buscar_repuesta, vista_eliminar_repuesta, vista_crear_respuesta

urlpatterns=[
    path('', lista_categorias.as_view(),name="preguntas"),
    path(r'registrar pregunta/(<pk>[0-9])(<tipo>[0-9])',vista_crear_preguntas,name="registrar_pregunta"),
    path(r'lista_pregunta/(<pk>[0-9])(<tipo>[0-9])\d+/', vista_lista_preguntas,name="lista_pregunta"),
    path(r'eliminar_pregunta/(<pk>[0-9])', vista_eliminar_pregunta, name="eliminar_pregunta"),

    path(r'registrar respuesta/(<pk>[0-9])\d+/', vista_crear_respuesta, name="registrar_respuesta"),
    path(r'buscar_repuesta/(<pk>[0-9])\d+/', vista_buscar_repuesta, name="buscar_repuesta"),
    path(r'eliminar_respuesta/(<pk>[0-9])\d+/', vista_eliminar_repuesta, name="eliminar_respuesta"),
]