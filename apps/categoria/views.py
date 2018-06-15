from django.shortcuts import render, render_to_response
from django.views.generic import View, ListView, CreateView
from django.db.models import Q
from .models import categoria
from .forms import nueva_categoria_form

# Create your views here.

# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'categoria/index.html')

class categorias(ListView):
    def get(self, request, *args, **kwargs):
        return render(request,'categoria/categoria.html')
    
class nueva_categoria(CreateView):
    template_name='categoria/nueva_categoria.html'    
    model= categoria
    form_class=nueva_categoria_form
    success_url=('/')
    def model_valid(self, form):
        return super(nueva_categoria, self).form_valid(form)
    def model_invalid(self, form):
        return super(nueva_categoria, self).form_invalid(form)
"""
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = categoria.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("categoria/busca_categoira.html", {
        "results": results,
        "query": query
    })
def busqueda(self,request):
    q = request.GET.get('q', '')
    eventos = categoria.objects.filter(ciudad__nombre__icontains=q)
    return render(request, 'categoria/busca_categoira.html', {'eventos': eventos})
"""