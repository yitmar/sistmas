from django.urls import include, path

from .views import lista_categorias, crear_preguntas, crear_respuesta, vista_preguntas_avanzada, vista_preguntas_basico, vista_preguntas_intermedio, vista_eliminar_pregunta

urlpatterns=[
    path('', lista_categorias.as_view(),name="preguntas"),
    path('registrar respuesta', crear_respuesta.as_view(),name="registrar_respuesta"),
    path('registrar pregunta', crear_preguntas.as_view(),name="registrar_pregunta"),
    path(r'^registrar_avanzado/(?P<pk>[0-9])\d/$', vista_preguntas_avanzada,name="pregunta_avanzada"),
    path(r'^registrar_intermedio/(?P<pk>[0-9])\d/$', vista_preguntas_intermedio,name="pregunta_intermedio"),
    path(r'^registrar_basico/(?P<pk>[0-9])\d/$',vista_preguntas_basico,name="pregunta_basico"),
    path(r'^eliminar_pregunta/(?P<pk>[0-9])\d/$', vista_eliminar_pregunta, name="eliminar_pregunta"),
]