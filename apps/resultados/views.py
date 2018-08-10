from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, DetailView, TemplateView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import formulario_cedula
from .models import resultado as Resultado
from apps.inicio.models import user as User

# Create your views here.

class vista_buscar_resultado(LoginRequiredMixin,View):
    login_url='/'
    redirect_field_name = 'redirect'
    def get(self, request, *args, **kwargs):
        if request.user.is_instructor:    
            return render(request,'resultados/index.html')
        else:
            message="no tiene permiso para para esta vista"
            return render(request,"inicio/index.html",{'message':message})
     
@login_required(login_url= '/')
def vista_mostras_resultado(request):
    if request.user.is_instructor:    
        if request.method== 'POST':
            resultados=request.POST['cedula']
            print(resultados)
            try:
                cedula_usuario=int(resultados)
                usuario=User.objects.filter(cedula_usuario=cedula_usuario)
                id_admin=0
                for admin in usuario:
                    id_admin=admin.id_admin
                    
                resultado=Resultado.objects.filter(id_admin=id_admin)
                return render(request, 'resultados/mostrar.html',{'resultado':resultado,'usuario':usuario})
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
    else:
        message="no tiene permiso para esta vista"
        return render(request,"inicio/index.html",{'message':message})

