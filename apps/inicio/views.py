from django.shortcuts import render, render_to_response, redirect, get_list_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.defaults import page_not_found
from django.http import Http404, HttpResponseNotFound  

from .models import user as User

from .forms import forms_login, formulario_registero_particpante, formilario_registro_instructor

# Create your views here.
#@login_required(login_url= '/')

class vista_registro_participante(CreateView):
    model = User
    form_class = formulario_registero_particpante
    template_name = 'inicio/registro_participante.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'particpante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        User = form.save()
        login(self.request, User)
        return redirect('vista_validacion_usuario')

class vista_registro_instructor(CreateView):
    model = User
    form_class = formilario_registro_instructor
    template_name = 'inicio/registro_instructor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'instructor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('vista_validacion_usuario')

@login_required(login_url= '/')
def vista_inicio(request):
    message=None
    cedula=request.user.cedula_usuario
    datos_user=User.objects.filter(cedula_usuario=cedula)
    if request.user.is_participante:
        message="bienvenido particpante"
    elif request.user.is_instructor:
        message="bienvenido instructor"        
    else:
        message="eres administrardor no puedes hacer entrer al sistema"
    return render(request,'inicio/index.html', {'message':message, 'datos_user':datos_user})

@login_required(login_url= '/')
def vista_validacion_usuario(request):
    message=None
    cedula=request.user.cedula_usuario
    datos_user=User.objects.filter(cedula_usuario=cedula)
    if request.user.is_participante:
        message="registro exito del pasticipante"
    elif request.user.is_instructor:
        message="registro exito del instructor"        
    else:
        message="eres administrardor no puedes hacer entrer al sistema "
    return render(request,'inicio/confimarcion_de_registro.html', {'message':message, 'datos_user':datos_user})

def vista_login(request):
    message= None
    if request.method == "POST":
        form= forms_login(request.POST)
        if form.is_valid():
            username=request.POST['cedula']
            password=request.POST['password']
            user=authenticate(username=username ,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message="te has logiado correctemante"
                    return redirect('bienvenido')
                else:
                    message="usuario inactivo"
            else:
                message="nombre de usuario y/o passsword incorrecto"
    else:
        form=forms_login
    return render(request,'inicio/login.html', {'message':message, 'form':form})

def vista_loguot(request):
    logout(request)
    return redirect('/')

def error404(request):
    data={}
    return render(request,'inicio/error404.html',data)

def control_error404(request):
    try:
        p = request.user.is_active
    except:
        raise Http404("Poll does not exist")
    return render(request, 'inicio/error404.html', {'poll': p})
  
def myView(request, param):  
  if not param:  
    return HttpResponseNotFound('<h1>dasdsadsa/h1>')  
  
  return render_to_response('inicio/error404.html')  