from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View, ListView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.inicio.decorador import instructor_required
from apps.inicio.models import user

from .models import categoria
from .forms import nueva_categoria_form

# Create your views here.

# Create your views here.
#@login_required(login_url= '/')

class inicio(LoginRequiredMixin, View):
    login_url='/'
    redirect_field_name = 'redirect'
    def get(self, request, *args, **kwargs):
        if request.user.is_instructor:
            return render(request,'categoria/index.html')
        else:
            message="no tiene permiso para para esta vista"
            return render(request,"inicio/index.html",{'message':message})

class vistas_categorias(LoginRequiredMixin, ListView):  
    login_url='/'
    redirect_field_name = 'redirect'
    template_name=('categoria/categoria.html')
    model=categoria
    queryset=categoria.objects.all()
    def get_context_data(self, **kwargs):
        context= super(vistas_categorias, self).get_context_data(**kwargs)
        context['total_questions']= categoria.objects.count()
        return context 
    
class nueva_categoria( LoginRequiredMixin, CreateView):
    login_url='/'
    redirect_field_name = 'redirect'
    template_name='categoria/nueva_categoria.html'    
    odel= categoria
    form_class=nueva_categoria_form
    success_url=('/categoria')
    def model_valid(self, form):
        return super(nueva_categoria, self).form_valid(form)
    def model_invalid(self, form):
        return super(nueva_categoria, self).form_invalid(form)

def vista_editar_categoria(request, pk):
    if request.user.is_instructor:
        Cate=categoria.objects.get(id_categoria=pk)
        if request.method=="POST":
            form=nueva_categoria_form(request.POST, instance=Cate)    
            if form.is_valid():
                form.save()
            return redirect('categoria')
        form=nueva_categoria_form(instance=Cate)

        return render(request,'categoria/nueva_categoria.html',{'form':form})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

def vista_eliminar_categoria(request,pk):
    if request.user.is_instructor:
        Categoria=categoria.objects.filter(id_categoria=pk)
        if request.method == 'POST':
            Categoria.delete()
            return redirect('categorias')
        return render(request, 'categoria/eliminar_categoria.html',{'Categoria':Categoria})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})
  


