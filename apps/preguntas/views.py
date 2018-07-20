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
    success_url=('/preguntas')
    def model_valid(self, form):
        return super(crear_preguntas, self).form_valid(form)
    def model_invalid(self, form):
        return super(crear_preguntas, self).form_invalid(form)

def vista_crear_preguntas(request, pk, tipo):
    if request.method == 'POST':

        form=preguntas_form(request.POST)
        if form.is_valid():
            nueva_pregunta=form.save(commit=False)
            nueva_pregunta.id_categoria=Categoria.objects.get(id_categoria=pk)
            nueva_pregunta.dificultad=tipo
            nueva_pregunta.save()
            return redirect("/preguntas")
        else:
            print("invalido")
    form=preguntas_form
    return render(request,'preguntas/registro.html',{'form':form})

def vista_lista_preguntas(request, pk, tipo):
    dificultad=tipo
    print(tipo)
    preguntas=pregunta.objects.filter(id_categoria=pk, dificultad=dificultad)
    return render(request,'preguntas/listas_preguntas.html',{'preguntas':preguntas,'dificultad':dificultad,'pk':pk})

def vista_eliminar_pregunta(request, pk):
    Pregunta=pregunta.objects.filter(id_pregunta=pk)
    if request.method == 'POST':
        Pregunta.delete()
        return redirect('/preguntas')
    return render(request, 'preguntas/eliminar_pregunta.html',{'Pregunta':Pregunta})

def vista_crear_respuesta(request,pk):
    if request.method =='POST':
        print(request.POST)
        form=respuesta_from(request.POST)
        if form.is_valid():
            print("valido")
            nueva_respuesta=form.save(commit=False)
            nueva_respuesta.id_pregunta=pregunta.objects.get(id_pregunta=pk)
            nueva_respuesta.save() 
            return redirect("/preguntas")
        else:
            print("invalido")
            pass    
    datos_preguntas=pregunta.objects.filter(id_pregunta=pk)
    form=respuesta_from    
    return render(request,'preguntas/registro_respuesta.html',{'form':form,'datos_preguntas':datos_preguntas})


def vista_buscar_repuesta(request, pk):
    id_pregunta=pk
    respuestas=respuesta.objects.filter(id_pregunta=id_pregunta)
    datos_preguntas=pregunta.objects.filter(id_pregunta=id_pregunta)
    return render(request, 'preguntas/ver_respuesta.html', {'respuestas':respuestas,'datos_preguntas':datos_preguntas,'id_pregunta':id_pregunta})

def vista_eliminar_repuesta(request, pk):
    print(pk)
    Respuestas=respuesta.objects.filter(id_respuesta=pk)
    if request.method == 'POST':
        Respuestas.delete()
        return redirect('/preguntas')
    return render(request, 'preguntas/eliminar_respuesta.html',{'Respuestas':Respuestas})