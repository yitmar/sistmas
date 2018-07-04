from django.urls import include, path

from .views import vista_buscar_resultado, vista_mostras_resultado

urlpatterns=[
    path(r'resultado',vista_buscar_resultado.as_view(), name='resultado'),
    path(r'buscar', vista_mostras_resultado,name='buscar'),
]
