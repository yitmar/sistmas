from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, DetailView, TemplateView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import formulario_cedula
from .models import resultado as Resultado

# Create your views here.
#@login_required(login_url= '/')

class vista_buscar_resultado(LoginRequiredMixin,View):
    login_url='/'
    redirect_field_name = 'redirect'
    def get(self, request, *args, **kwargs):
        return render(request,'resultados/index.html')

@require_http_methods(["GET", "POST"])
@login_required(login_url= '/')
def vista_mostras_resultado(request):
    if request.method== 'POST':
        resultados=request.POST['buscar']
        print(resultados)
        try:
            id_participante=int(resultados)
            resultado=Resultado.objects.filter(id_participante=id_participante)
            return render(request, 'resultados/mostrar.html',{'resultado':resultado})
        except:
            print("Debes introducir una cadena que sea un número")
            return render(request,'resultados/index.html')
        else:
            print("error")
            return render(request,'resultados/index.html')
    else:
        print("no es post")
        return render(request,'resultados/index.html')
    return render(request,'resultados/index.html')
