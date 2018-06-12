from django.urls import include, path

from .views import registro

urlpatterns=[
    path('', registro, name="registro"),
]
