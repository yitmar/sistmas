"""sistema_preguntas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auditoria/',include('apps.auditoria.urls')),    
    path('categoria/',include('apps.categoria.urls')),
    path(r'',include('apps.inicio.urls')),
    path('preguntas/',include('apps.preguntas.urls')),
    path('pruebas/',include('apps.pruebas.urls')),
    path('resultados/',include('apps.resultados.urls')),
    path('users/',include('apps.users.urls')),
    path('administracion/',include('apps.administracion.urls')),
   
]
