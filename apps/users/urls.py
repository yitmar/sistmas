from django.urls import include, path

from .views import registro

urlpatterns=[
    path('', registro.as_view(), name="registro"),    
]
