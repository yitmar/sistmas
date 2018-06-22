"""

from django.http import JsonResponse
from apps.preguntas.models import dificultad as Dificultad
from apps.categoria.models import categoria as Categoria
from apps.administracion.models import administrador
from .models import prueba
from .forms import form_prueba_prueba

def get_categorias(request):
    id_categoria = request.GET.get('id_categoria')
    categoria = Categoria.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_categoria:
        categoria = Categoria.objects.filter(id_categoria=id_categoria)   
    for categori in categoria:
        options += '<option value="%s">%s</option>' % (
            categori.pk,
            categori.categori
        )
    response = {}
    response['categori'] = options
    return JsonResponse(response)


def get_dificultad(request):
    id_dificultad = request.GET.get('id_dificultad')
    dificultad = Dificultad.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_dificultad:
        dificultad = Dificultad.objects.filter(id_dificultad=id_dificultad)   
    for localidad in dificultad:
        options += '<option value="%s">%s</option>' % (
            localidad.pk,
            localidad.localidad
        )
    response = {}
    response['localidades'] = options
    return JsonResponse(response)
    """