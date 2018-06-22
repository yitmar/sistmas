from django.shortcuts import render, render_to_response
from django.views.generic import View, ListView, CreateView, DetailView
from django.db.models import Q

from apps.categoria.models import categoria as Categoria

from .models import prueba
from .forms import formulario_crear_prueba, formulario_asignar_prueba, formulario_realizar_prueba
 
# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'pruebas/index.html')

class asignar_prueba(CreateView):
    template_name=('pruebas/asignar_prueba.html')
    model=prueba
    form_class=formulario_asignar_prueba
    success_url=('/')
    def model_valid(self, form):
        return super(asignar_prueba, self).form_valid(form)
    def model_invalid(self, form):
        return super(asignar_prueba, self).form_invalid(form)

class crear_prueba(CreateView):
    template_name=('pruebas/crear_pruebas.html')
    model=prueba
    form_class=formulario_crear_prueba
    success_url=('/')
    lista=[]
    """
    def model_valid(self, form):
        if form.form_valid(form):
            form.save(commit=False)
            return print(form)
    def model_invalid(self, form):
        lista=[]
        print(form)
        return super(crear_prueba, self).form_invalid(form)
    """
""" medoto de ajax pendiente
    def vista_ubicacion(request):
        form = form_prueba_prueba()
        if request.method == 'POST':
            form = form_prueba_prueba(request.POST)
            if form.is_valid():
                # Guardar los datos
                url = reverse('/')
                return HttpResponseRedirect(url)
        return render(request, 'pruebas/prue.html', {
            'form': form
        })
    """
"""
    def search(request):
        query = request.GET.get('q', '')
        if query:
            qset = (
                Q(id_categoria=query) |
                Q(id_dificultad=query) 
            )
            results = prueba.objects.filter(qset).distinct()
        else:
            results = []
        return render_to_response("pruebas/crear.html", {
            "results": results,
            "query": query
        })
"""

class lista_prueba(ListView):
    template_name=('pruebas/listar_pruebas.html')
    model=Categoria
    queryset=prueba.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_prueba, self).get_context_data(**kwargs)
        context['total_questions']= prueba.objects.count()
        return context

class datos(DetailView):
    template_name=('pruebas/ver_prueba.html')
    model= prueba
    success_url=('/')
    
    