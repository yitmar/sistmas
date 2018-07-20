from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View, ListView, CreateView, DeleteView

from .models import categoria
from .forms import nueva_categoria_form

# Create your views here.

# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'categoria/index.html')

class vistas_categorias(ListView):    
    template_name=('categoria/categoria.html')
    model=categoria
    queryset=categoria.objects.all()
    def get_context_data(self, **kwargs):
        context= super(vistas_categorias, self).get_context_data(**kwargs)
        context['total_questions']= categoria.objects.count()
        return context    
    
class nueva_categoria(CreateView):
    template_name='categoria/nueva_categoria.html'    
    model= categoria
    form_class=nueva_categoria_form
    success_url=('/categoria')
    def model_valid(self, form):
        return super(nueva_categoria, self).form_valid(form)
    def model_invalid(self, form):
        return super(nueva_categoria, self).form_invalid(form)

def vista_eliminar_categoria(request,pk):
    Categoria=categoria.objects.filter(id_categoria=pk)
    if request.method == 'POST':
        Categoria.delete()
        return redirect('/')
    return render(request, 'categoria/eliminar_categoria.html',{'Categoria':Categoria})
