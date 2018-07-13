from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, DetailView
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from apps.resultados.models import resultado
from django.core.mail import EmailMessage
from random import randint

from apps.categoria.models import categoria as Categoria
from apps.preguntas.models import pregunta, respuesta
from apps.users.models import participante

from .models import prueba as Prueba
from .forms import formulario_crear_prueba, formulario_asignar_prueba, formulario_realizar_prueba
 
# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'pruebas/index.html')

class asignar_prueba(CreateView):  
    template_name=('pruebas/asignar_prueba.html')
    model=Prueba
    form_class=formulario_asignar_prueba
    success_url=('/')
    def model_valid(self, form):
        return super(asignar_prueba, self).form_valid(form)
    def model_invalid(self, form):
        return super(asignar_prueba, self).form_invalid(form)

@require_http_methods(["GET", "POST"])
def crear_prueba(request):
    if request.method == 'POST':
        form=formulario_crear_prueba(request.POST)
        if form.is_valid():
            valor=[]
            valor.append(2)
            valor.append(3)
            preguntas=[]
            preguntas=request.POST['preguntas']
            print (preguntas)
            nueva_prueba=form.save(commit=False)
            nueva_prueba.arreglo_valor=valor
            nueva_prueba.arreglo_preguntas=preguntas
            #print (nueva_prueba)
            nueva_prueba.save()
            return render(request,'pruebas/crear_pruebas.html')
    elif request.method == 'GET':
        form=formulario_crear_prueba    
        return render(request,'pruebas/crear_pruebas.html',{'form':form})
    else:
        form=formulario_crear_prueba        
        return render(request,'pruebas/crear_pruebas.html',{'form':form})

class lista_prueba(ListView):
    template_name=('pruebas/listar_pruebas.html')
    model=Categoria
    queryset=Prueba.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_prueba, self).get_context_data(**kwargs)
        return context


def datos(request,pk):
    prueba=Prueba.objects.filter(id_prueba=pk)
    arreglo_pregunta=[]
    preguntaa=[]
    respuestas=[]
    cantidad_pregunta=0
    id_participante=0
    for item in prueba:
        id_participante=item.id_participante
        id_dificultad=item.id_dificultad
        id_categoria=item.id_categoria
        cantidad_pregunta=item.cantidad_pregunta
        arreglo_preguntas=item.arreglo_preguntas
        q=0
        while q < cantidad_pregunta:
            arreglo_pregun=len(arreglo_preguntas)-1
            numero_pregunta_rando= randint(0,arreglo_pregun)
            arreglo_pregunta.append(arreglo_preguntas[numero_pregunta_rando])
            id_pregunta=arreglo_pregunta[numero_pregunta_rando]

            preguntaa=pregunta.objects.filter(id_pregunta=id_pregunta)
            for pre in preguntaa:
                nombre=pre.nombre_pregunta
                tipo_pregunta=pre.tipo_pregunta
                
            respuestas=respuesta.objects.filter(id_pregunta=id_pregunta)
            for res in respuestas:
                id_respuesta=res.id_respuesta
                nombre_respuesta=res.nombre_respuesta
                tipo_respuesta=res.tipo_respuesta
            q=1+q
    if request.method == 'POST':
        a=0
        nota_evaluacion=0
        nota=0
        arreglo_respuesta=[]
        while a < cantidad_pregunta:
            b=request.POST['respuesta']
            arreglo_respuesta.append(b)
            consulta_nota=respuesta.objects.filter(id_respuesta=b)
            for consulta_de in consulta_nota:
                if(consulta_de.tipo_respuesta):
                    nota=1
            nota_evaluacion=nota+nota_evaluacion  
            a=a+1
        nueva_resultado=resultado(id_participante=id_participante,id_categoria=id_categoria,arreglo_preguntas=arreglo_pregunta,arreglo_respuesta=arreglo_respuesta,nota_evaluacion=nota_evaluacion)
        nueva_resultado.save()
        send_email(request)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'pruebas/ver_prueba.html',
        {'preguntaa':preguntaa,'respuestas':respuestas,'prueba':prueba},)

def send_email(request):
    msg=EmailMessage(subject="prueba",from_email="yitmar.14151819@gmail.com",to=['yitmar.14151819@hotmail.com'])
    msg.template_name='pantilla de prueba'
    msg.send()
