from django.shortcuts import render, redirect
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

def vista_preguntas_avanzada(request, pk):
    preguntas=pregunta.objects.filter(id_categoria=pk, dificultad=3)
    return render(request,'preguntas/listas_preguntas.html',{'preguntas':preguntas})

def vista_preguntas_intermedio(request, pk):
    preguntas=pregunta.objects.filter(id_categoria=pk, dificultad=2)
    return render(request,'preguntas/listas_preguntas.html',{'preguntas':preguntas})

def vista_preguntas_basico(request, pk):
    preguntas=pregunta.objects.filter(id_categoria=pk, dificultad=1)
    return render(request,'preguntas/listas_preguntas.html',{'preguntas':preguntas})

def vista_eliminar_pregunta(request, pk):
    Pregunta=pregunta.objects.filter(id_pregunta=pk)
    if request.method == 'POST':
        Pregunta.delete()
        return redirect('/')
    return render(request, 'preguntas/eliminar_pregunta.html',{'Pregunta':Pregunta})

    