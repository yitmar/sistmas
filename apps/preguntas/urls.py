from django.urls import include, path

from .views import lista_categorias, crear_preguntas, crear_respuesta

urlpatterns=[
    path('', lista_categorias.as_view(),name="preguntas"),
    path('registrar respuesta', crear_respuesta.as_view(),name="registrar_respuesta"),
    path('registrar pregunta', crear_preguntas.as_view(),name="registrar_pregunta"),
    path('registrar avanzado', crear_preguntas.as_view(),name="pregunta_avanzada"),
    path('registrar intermedio', crear_preguntas.as_view(),name="pregunta_intermedio"),
    path('registrar basico', crear_preguntas.as_view(),name="pregunta_basico"),
]