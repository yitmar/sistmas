from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, DetailView
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage
from random import randint

from apps.categoria.models import categoria as Categoria
from apps.preguntas.models import pregunta, respuesta, dificultad
from apps.users.models import participante
from apps.resultados.models import resultado

from .models import prueba as Prueba, prueba_presona
from .forms import formulario_crear_prueba, formulario_asignar_prueba, formulario_realizar_prueba
 
# Create your views here.
#@login_required(login_url= '/')

class inicio(ListView):
    template_name=('pruebas/lista_categoria.html')
    model=Categoria
    queryset=Categoria.objects.all()
    def get_context_data(self, **kwargs):
        context= super(inicio, self).get_context_data(**kwargs)
        context['total_questions']= Categoria.objects.count()
        return context

def vista_listar_pruebas(request, pk, tipo):
    id_categoria=pk
    id_dificultad=tipo
    prueba=Prueba.objects.filter(id_categoria=pk, id_dificultad=id_dificultad)
    print(prueba)
    return render(request,'pruebas/listas_crear_preguntas.html',{'prueba':prueba,'id_categoria':id_categoria,'id_dificultad':id_dificultad})

def vista_buscar_preguntas(request, pk):
    id_prueba=pk
    prueba=Prueba.objects.filter(id_prueba=id_prueba)
    arreglo_preguntas=[]
    for preu in prueba:
        arreglo_preguntas=preu.arreglo_preguntas
    rango=len(arreglo_preguntas)
    x=0
    preguntas=[]
    while x < rango:
        pre=pregunta.objects.get(id_pregunta=arreglo_preguntas[x])
        preguntas.append(pre)
        print(preguntas)
        x+=1
    return render(request,'pruebas/lista_preguntas.html',{'preguntas':preguntas})

def vista_crear_prueba(request,pk,tipo):
    id_categoria=pk
    id_dificultad=tipo
    if request.method == 'POST':
        form=formulario_crear_prueba(request.POST)
        if form.is_valid():
            arreglo_preguntass=request.POST.getlist('preguntas')
            arreglo_valor=request.POST.getlist('arreglo')
            nueva_prueba=form.save(commit=False)
            nueva_prueba.id_categoria=Categoria.objects.get(id_categoria=id_categoria)
            nueva_prueba.id_dificultad=dificultad.objects.get(id_dificultad=id_dificultad)
            nueva_prueba.arreglo_preguntas=arreglo_preguntass
            nueva_prueba.arreglo_valor=arreglo_valor
            nueva_prueba.save()
            return redirect('/')
        else:
            print("invalido")
            pass
    elif request.method == 'GET':
        preguntas=pregunta.objects.filter(id_categoria=pk,dificultad=tipo)
        form=formulario_crear_prueba    
        return render(request,'pruebas/crear_pruebas.html',{'form':form,'preguntas':preguntas})
    else:
        print("otros")
        form=formulario_crear_prueba        
        return render(request,'pruebas/crear_pruebas.html',{'form':form})

def vista_eliminar_pregunta(request, pk):
    pass

class asignar_prueba(CreateView):  
    template_name=('pruebas/asignar_prueba.html')
    model=Prueba
    form_class=formulario_asignar_prueba
    success_url=('/')
    def model_valid(self, form):
        return super(asignar_prueba, self).form_valid(form)
    def model_invalid(self, form):
        return super(asignar_prueba, self).form_invalid(form)

class lista_prueba(ListView):
    template_name=('pruebas/listar_pruebas.html')
    model=Categoria
    queryset=Prueba.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_prueba, self).get_context_data(**kwargs)
        return context

def vista_ver_pruebas_asignadas(request):
    valor=1
    participantes=valor
    pruebas=prueba_presona.objects.filter(id_participante=participantes)
    lista_prueba=[]
    for prue in pruebas:
        id_prueba=prue.id_prueba
        lista_prueba.append(id_prueba)
    return render(request,'pruebas/listar_pruebas.html',{'pruebas':pruebas,'lista_prueba':lista_prueba})

def datos(request,pk):
    pruebs_presona=prueba_presona.objects.filter(id_prueba_presona=pk)
    arreglo_respuesta=[]
    durancion_pruaba=0
    cantidad_pregunta=0
    arreglo_pruebas=[]
    arreglo_valor_respuesta=[]
    arreglo_pregunta_respuesta=[]
    id_categoria=0
    id_participante=0
    arreglo_pregunta=[]
    arreglo_preguntas=[]

    prueba_presentar=[]

    for item in pruebs_presona:
        id_participante=item.id_participante
        id_prueba=item.id_prueba
        p=str(id_prueba)
        pruebas=Prueba.objects.filter(id_prueba=p)
        for prue in pruebas:
            durancion_pruaba=prue.durancion_pruaba
            cantidad_pregunta=prue.cantidad_pregunta
            arreglo_preguntas=prue.arreglo_preguntas
            arreglo_valor=prue.arreglo_valor
            id_categoria=prue.id_categoria
        q=0
        arreglo_pregun=len(arreglo_preguntas)-1

        while q < cantidad_pregunta:
            numero_pregunta_rando=randint(0,arreglo_pregun)
            id_pregunta=arreglo_preguntas[numero_pregunta_rando]
            
            nuemro_pregunta=q+1
            prueba_presentar.append(nuemro_pregunta)

            arreglo_valor_respuesta.append(arreglo_valor[numero_pregunta_rando])
            arreglo_pregunta_respuesta.append(id_pregunta)

            preguntaa=pregunta.objects.filter(id_pregunta=id_pregunta)
            arreglo_pregunta.append(preguntaa)
            for pregun in preguntaa:
                id_pregunta=pregun.id_pregunta
                nombre_pregunta=pregun.nombre_pregunta
                prueba_presentar.append(nombre_pregunta)

            respuestas=respuesta.objects.filter(id_pregunta=id_pregunta)
            arreglo_respuesta.append(respuestas)
            print(len(respuestas))
            for res in respuestas:
                id_respuesta=res.id_respuesta
                nombre_respuesta=res.nombre_respuesta
                prueba_presentar.append(id_respuesta)
                prueba_presentar.append(nombre_respuesta)                

            q=1+q

    if request.method == 'POST':
        a=0
        nota_evaluacion=0
        nota=0
        arreglo_respuesta=[]
        print(request.POST)
        while a < cantidad_pregunta:
            pregunta_id=arreglo_pregunta_respuesta[a]
            print(pregunta_id)
            respuesta_pregunta=request.POST
            arreglo_respuesta.append(respuesta_pregunta)
            nota_evaluacion=nota+nota_evaluacion  
            a=a+1
        nueva_resultado=resultado(id_participante=id_participante,id_categoria=id_categoria,arreglo_preguntas=arreglo_pregunta_respuesta,arreglo_respuesta=arreglo_respuesta,nota_evaluacion=nota_evaluacion)
        #nueva_resultado.save()
        #send_email(request)
        return redirect('/')
    else:
        print(prueba_presentar)
        return render(request, 'pruebas/ver_prueba.html',
        {'arreglo_pregunta':arreglo_pregunta,'arreglo_respuesta':arreglo_respuesta,'pruebs_presona':pruebs_presona,'arreglo_pruebas':arreglo_pruebas,'prueba_presentar':prueba_presentar },)

def send_email(request):
    msg=EmailMessage(subject="prueba",from_email="yitmar.14151819@gmail.com",to=['yitmar.14151819@hotmail.com'])
    msg.template_name='pantilla de prueba'
    msg.send()