from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login,logout
from django.views.generic import CreateView
from django.contrib.auth.views import login, LogoutView

from .models import user as User

from .forms import forms_login, formulario_registero_particpante, formilario_registro_instructor

# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'inicio/index.html')

class vista_registro_participante(CreateView):
    model = User
    form_class = formulario_registero_particpante
    template_name = 'inicio/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'particpante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        User = form.save()
        login(self.request, User)
        return redirect('lista_prueba')

class vista_registro_instructor(CreateView):
    model = User
    form_class = formilario_registro_instructor
    template_name = 'inicio/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'instructor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('lista_prueba')

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
                    login(request, User)
                    message="te has logiado correctemante"
                else:
                    message="usuario inactivo"
            else:
                message="nombre de usuario y/o passsword incorrecto"
    else:
        form=forms_login
    return render(request,'inicio/login.html', {'message':message, 'form':form})

