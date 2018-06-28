from django.urls import include, path

from .views import inicio

urlpatterns=[
    path('resultado', inicio.as_view(),name='resultado'),
]
