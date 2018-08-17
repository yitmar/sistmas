from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.categoria.models import categoria as Categoria
from apps.resultados.models import resultado as Resultado
from apps.pruebas.models import prueba as Prueba

from .models import pregunta, respuesta
from .froms import preguntas_form, respuesta_from


# Create your views here.
class lista_categorias(LoginRequiredMixin, ListView):
    login_url='/'
    redirect_field_name = 'redirect'
    template_name=('preguntas/index.html')
    model=Categoria
    queryset=Categoria.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_categorias, self).get_context_data(**kwargs)
        context['total_questions']= Categoria.objects.count()
        return context

class crear_preguntas(LoginRequiredMixin, CreateView):
    login_url='/'
    redirect_field_name = 'redirect'
    def get(self, request, *args, **kwargs):
        if request.user.is_instructor:
            template_name='preguntas/registro.html'    
            model= pregunta
            form_class=preguntas_form
            success_url=('/preguntas')
            def model_valid(self, form):
                return super(crear_preguntas, self).form_valid(form)
            def model_invalid(self, form):
                return super(crear_preguntas, self).form_invalid(form)
        else:
            message="no tiene permiso para para esta vista"
            return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_crear_preguntas(request, pk, tipo):
    if request.user.is_instructor:
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
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_lista_preguntas(request, pk, tipo):
    if request.user.is_instructor:
        dificultad=tipo
        print(tipo)
        preguntas=pregunta.objects.filter(id_categoria=pk, dificultad=dificultad)
        return render(request,'preguntas/listas_preguntas.html',{'preguntas':preguntas,'dificultad':dificultad,'pk':pk})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_editar_pregunta(request, pk):
    if request.user.is_instructor:
        preg=pregunta.objects.get(id_pregunta=pk)
        if request.method=="POST":
            form=preguntas_form(request.POST, instance=preg)    
            if form.is_valid():
                form.save()
            return redirect('/preguntas')
        form=preguntas_form(instance=preg)

        return render(request,'preguntas/registro.html',{'form':form})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_eliminar_pregunta(request, pk):
    if request.user.is_instructor:    
        Pregunta=pregunta.objects.filter(id_pregunta=pk)
        nombre_pregunta=0
        for pregun in Pregunta:
            nombre_pregunta=pregun.nombre_pregunta
        if request.method == 'POST':
            prueba=Prueba.objects.all()
            for prue in prueba:
                pr=prue.arreglo_preguntas
                for pre in pr:
                    if pre==pk:
                        message="no se puede eliminar esta pregunta ya que posee una prueba ya realizada"
                        return render(request, 'preguntas/eliminar_pregunta.html',{'Pregunta':Pregunta, 'message':message})
            resultado=Resultado.objects.all()
            for result in resultado:
                re=result.arreglo_preguntas
                for relta in re:
                    if (str(relta))==(str(nombre_pregunta)):
                        message="no se puede eliminar esta pregunta ya que posee una prueba ya realizada"
                        return render(request, 'preguntas/eliminar_pregunta.html',{'Pregunta':Pregunta, 'message':message})
            Pregunta.delete()
            return redirect('/preguntas')
        return render(request, 'preguntas/eliminar_pregunta.html',{'Pregunta':Pregunta})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_crear_respuesta(request,pk):
    if request.user.is_instructor:    
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
               
        datos_preguntas=pregunta.objects.filter(id_pregunta=pk)
        form=respuesta_from    
        return render(request,'preguntas/registro_respuesta.html',{'form':form,'datos_preguntas':datos_preguntas})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_buscar_repuesta(request, pk):
    if request.user.is_instructor:    
        id_pregunta=pk
        respuestas=respuesta.objects.filter(id_pregunta=id_pregunta)
        datos_preguntas=pregunta.objects.filter(id_pregunta=id_pregunta)
        return render(request, 'preguntas/ver_respuesta.html', {'respuestas':respuestas,'datos_preguntas':datos_preguntas,'id_pregunta':id_pregunta})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_editar_respuesta(request, pk):
    if request.user.is_instructor:
        resp=respuesta.objects.get(id_respuesta=pk)
        if request.method=="POST":
            form=respuesta_from(request.POST, instance=resp)    
            if form.is_valid():
                form.save()
            return redirect('/preguntas')
        form=respuesta_from(instance=resp)
        return render(request,'preguntas/registro_respuesta.html',{'form':form})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_eliminar_repuesta(request, pk):
    if request.user.is_instructor:    
        print (pk)
        Respuestas=respuesta.objects.filter(id_respuesta=pk)
        if request.method == 'POST':
            Respuestas.delete()
            return redirect('/preguntas')
        return render(request, 'preguntas/eliminar_respuesta.html',{'Respuestas':Respuestas})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})
