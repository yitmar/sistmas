from django.shortcuts import render
from django.views.generic import View, ListView, CreateView

from apps.categoria.models import categoria as Categoria
from .models import pregunta, respuesta
from .froms import preguntas_form, respuesta_from

# Create your views here.
#@login_required(login_url= '/')
class lista_categorias(ListView):
    template_name=('preguntas/index.html')
    model=Categoria
    queryset=Categoria.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_categorias, self).get_context_data(**kwargs)
        context['total_questions']= Categoria.objects.count()
        return context

class crear_preguntas(CreateView):
    template_name='preguntas/registro.html'    
    model= pregunta
    form_class=preguntas_form
    success_url=('/')
    def model_valid(self, form):
        return super(crear_preguntas, self).form_valid(form)
    def model_invalid(self, form):
        return super(crear_preguntas, self).form_invalid(form)

class crear_respuesta(CreateView):
    template_name='preguntas/registro_respuesta.html'    
    model= respuesta
    form_class=respuesta_from
    success_url=('/')
    def model_valid(self, form):
        return super(crear_respuesta, self).form_valid(form)
    def model_invalid(self, form):
        return super(crear_respuesta, self).form_invalid(form)

"""
    class crear_preguntas(CreateView):
        template_name='preguntas/registro.html'    
        model= pregunta
        form_class=preguntas_form
        success_url=('preguntas/registro_respuesta')
        def model_valid(self,request, form):
            if super(crear_preguntas, self).form_valid(form):
                f = preguntas_form(request.POST)
                new_author = f.save(commit=False)
                new_author.some_
                return 
        def model_invalid(self, form):
            return super(crear_preguntas, self).form_invalid(form)
"""