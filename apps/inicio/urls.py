"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
  
"""
from django.urls import include, path
from .views import inicio, vista_login, vista_registro_participante, vista_registro_instructor


urlpatterns=[
    path('', vista_login ,name='inicio'),
    path('registro_instructor/', vista_registro_instructor.as_view(), name='registro_instructor'),
    path('registro_participante/', vista_registro_participante.as_view(), name='registro_participante'),
]
