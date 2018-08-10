"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import include, path
from django.conf.urls import handler404
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from .views import vista_login, vista_registro_participante, vista_registro_instructor, vista_loguot, vista_inicio, error404, myView


urlpatterns=[
    path('', vista_login ,name='inicio'),
    path('bienvenido', vista_inicio,name='bienvenido'),
    path('registro_instructor/', vista_registro_instructor.as_view(), name='registro_instructor'),
    path('registro_participante/', vista_registro_participante.as_view(), name='registro_participante'),
    path('logout', vista_loguot, name='logout'),
    path('resest/password_reset',password_reset,{'template_name':'inicio/password_reset_form.html','email_template_name':'inicio/password_reset_email.html'},name='password_reset'),
    path('resert/password_reset_done', password_reset_done,{'template_name':'inicio/password_reset_done.html'},name='password_reset_done'),
    path('reset/(?p<uidb64>[0-9A-Za-z_\-]+/(?P<token>.+)/$', password_reset_confirm,{'template_name':'inicio/password_reset_confim.html'},name='password_reset_confirm'),
    path('reset/done',password_reset_complete,{'template_name':'inicio/password_reset_complete.html'},name='password_reset_complete'),
]

