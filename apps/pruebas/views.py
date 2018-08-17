from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, DetailView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from random import randint

from apps.categoria.models import categoria as Categoria
from apps.preguntas.models import pregunta, respuesta, dificultad
from apps.resultados.models import resultado
from apps.inicio.models import user as User

from .models import prueba as Prueba, prueba_presona
from .forms import formulario_crear_prueba, formulario_realizar_prueba
 
# Create your views here.

class inicio(LoginRequiredMixin, ListView):
    login_url='/'
    redirect_field_name = 'redirect'
    template_name=('pruebas/lista_categoria.html')
    model=Categoria
    queryset=Categoria.objects.all()
    def get_context_data(self, **kwargs):
        context= super(inicio, self).get_context_data(**kwargs)
        context['total_questions']= Categoria.objects.count()
        return context

@login_required(login_url= '/')
def vista_listar_pruebas(request, pk, tipo):
    if request.user.is_instructor:
        id_categoria=pk
        id_dificultad=tipo
        prueba=Prueba.objects.filter(id_categoria=pk, id_dificultad=id_dificultad)
    
        return render(request,'pruebas/listas_crear_preguntas.html',{'prueba':prueba,'id_categoria':id_categoria,'id_dificultad':id_dificultad})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_buscar_preguntas(request, pk):
    if request.user.is_instructor:
        id_prueba=pk
        prueba=Prueba.objects.filter(id_prueba=id_prueba)
        arreglo_preguntas=[]
        for preu in prueba:
            arreglo_preguntas=preu.arreglo_preguntas
        rango=len(arreglo_preguntas)
        x=0
        preguntas=[]
        while x < rango:
            pre=pregunta.objects.filter(id_pregunta=arreglo_preguntas[x])
            preguntas.append(pre)
            #print(preguntas)
            x+=1
        print(preguntas)
        return render(request,'pruebas/lista_preguntas.html',{'preguntas':preguntas})

    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= 'categorias')
def vista_crear_prueba(request,pk,tipo):
    pk=pk
    tipo=tipo
    if request.user.is_instructor:
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
                return vista_listar_pruebas(request,pk,tipo)
            else:
                print("invalido")
                pass
        elif request.method == 'GET':
            arreglo_preguntas=[]
            preguntas=pregunta.objects.filter(id_categoria=pk,dificultad=tipo)
            for pre in preguntas:
                id_pregunta=pre.id_pregunta
                respuestas=respuesta.objects.filter(id_pregunta=id_pregunta).order_by("tipo_respuesta")
                cantidad_respuest=len(respuestas)
                if cantidad_respuest >0:
                    for res in respuestas:
                        if res.tipo_respuesta:
                            pregunta_valida=pregunta.objects.get(id_pregunta=id_pregunta)
                            arreglo_preguntas.append(pregunta_valida)
           
            form=formulario_crear_prueba 
            form=formulario_crear_prueba    
            return render(request,'pruebas/crear_pruebas.html',{'form':form,'arreglo_preguntas':arreglo_preguntas})
        else:
            print("otros")
            form=formulario_crear_prueba        
            return render(request,'pruebas/crear_pruebas.html',{'form':form})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_eliminar_prueba(request, pk):

    if request.user.is_instructor:    
        prueba=Prueba.objects.filter(id_prueba=pk)
        if request.method == 'POST':
            prueba.delete()
            return redirect('pruebas')
        return render(request,'pruebas/eliminar_prueba.html',{'prueba':prueba})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_Asignar_prueba(request):
    if request.user.is_instructor: 
        if request.method=="POST":
            nueva_asignacion=prueba_presona(id_admin=request.POST['usuarios'],id_prueba=request.POST['prueba'])
            
            nueva_asignacion.save()
            return redirect('categoria') 
        elif request.method== 'GET':

            pruebas=Prueba.objects.all()
            lista_pruebas=[]
            for prue in pruebas:
                id_prueb=prue.id_prueba            
                nombre_prueba=prue.nombre_prueba
                listaaa=(id_prueb,nombre_prueba)
                lista_pruebas.append(listaaa)

            participante=True
            useuarios=User.objects.filter(is_participante=participante)
            lista_usuarios=[]
            for prue in useuarios:
                id_admin=prue.cedula_usuario            
                nombre_usuario=prue.nombre_usuario
                listaa=(id_admin,nombre_usuario)
                lista_usuarios.append(listaa)
            return render(request,'pruebas/asignar_prueba.html',{'lista_pruebas':lista_pruebas,'lista_usuarios':lista_usuarios})
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})
    
class lista_prueba(LoginRequiredMixin, ListView):
    login_url='/'
    redirect_field_name = 'redirect'
    template_name=('pruebas/listar_pruebas.html')
    model=Categoria
    queryset=Prueba.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_prueba, self).get_context_data(**kwargs)
        return context

@login_required(login_url= '/')
def vista_ver_pruebas_asignadas(request):
    if request.user.is_participante:
        participantes=request.user.cedula_usuario
        try:
            pruebas=prueba_presona.objects.filter(id_admin=participantes)
            lista_prueba=[]
            for prue in pruebas:
                id_prueba=prue.id_prueba
                prueba=Prueba.objects.filter(id_prueba=id_prueba)
                for pru in prueba:
                    pru.id_categoria
                    lista_prueba.append(id_prueba)
            return render(request,'pruebas/listar_pruebas.html',{'pruebas':pruebas,'lista_prueba':lista_prueba})
        except TypeError:
            message="no error no hay prueba asisnada"
            return render(request,'pruebas/listar_pruebas.html',{'message':message})            
    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def vista_realizar_prueba(request,pk):
    if request.user.is_participante:
        
        pruebs_presona=prueba_presona.objects.filter(id_prueba_presona=pk)

        #datos para la evaluacion
        cantidad_pregunta=0
        id_categoria=0
        id_admin=0
        arreglo_valor=[]
        #arreglo_preguntas=[]
        #datos para la prueba
        durancion_pruaba=0
        arreglos_prueba=[]

        arreglo_pruebas=[]
        arreglo_pregunta=[]
        arreglo_preguntas=[]

        for item in pruebs_presona:
            id_admin=item.id_admin
            id_prueba=item.id_prueba
            p=str(id_prueba)
            pruebas=Prueba.objects.filter(id_prueba=p)
            for prue in pruebas:
                durancion_pruaba=prue.durancion_pruaba
                cantidad_pregunta=prue.cantidad_pregunta
                arreglo_preguntas=prue.arreglo_preguntas
                arreglo_valor=prue.arreglo_valor
                id_categoria=prue.id_categoria
            rango_pregunta=len(arreglo_preguntas)-1

        if request.method == 'POST':
            a=0
            nota_evaluacion=0
            nota=0
            arreglo_respuesta=[]
            numero_pregunta=1
            while a < cantidad_pregunta:
                carater_pregunta=str(numero_pregunta)
                try:
                    respuesta_pregunta=request.POST[carater_pregunta]
                    arreglo_respuesta.append(respuesta_pregunta)
                    datos_respuesta=respuesta.objects.filter(id_respuesta=respuesta_pregunta)
                    for res in datos_respuesta:
                        id_pregunta=res.id_pregunta
                        tipo_respuesta=res.tipo_respuesta
                    arreglo_pregunta.append(id_pregunta)
                
                    if tipo_respuesta:
                        print("correcta")
                        condi=0
                        while condi < rango_pregunta:
                            print("pri")
                            for pre in arreglo_preguntas:
                                print (pre)
                                print (id_pregunta)
                                datos_pregunta=pregunta.objects.filter(nombre_pregunta=id_pregunta)
                                for pregun in datos_pregunta:
                                    nombre_pregunta=pregun.nombre_pregunta
                                print(nombre_pregunta)
                            if nombre_pregunta==str(id_pregunta):
                                print("valido")
                                nota=arreglo_valor[condi]
                                condi=rango_pregunta+1
                            condi=1+condi
                    else:
                        print("incorreco")
                        nota=0
                except KeyError:
                    print("not")
                    nota=0
                nota_evaluacion=nota+nota_evaluacion
                numero_pregunta=numero_pregunta+1
                a=a+1
            
            participante=User.objects.get(cedula_usuario =id_admin)

            print("guardar")
            print (id_admin)
            print (id_categoria)
            print (arreglo_pregunta)
            print (nota_evaluacion)
            print (arreglo_respuesta)    
            nueva_resultado=resultado(id_admin=participante,
                                    id_categoria=id_categoria,
                                    arreglo_preguntas=arreglo_pregunta,
                                    arreglo_respuesta=arreglo_respuesta,
                                    nota_evaluacion=nota_evaluacion)
            nueva_resultado.save()
            #send_email(request)
            return redirect('bienvenido')
        else:
            q=0
            arreglos_rando_numeros=[]

            while q < cantidad_pregunta:
                numero_pregunta_rando=randint(0,rango_pregunta)
                x=0

                if len(arreglos_rando_numeros)==0:
                    arreglo_contenido_pregunta=[]
                    arreglos_rando_numeros.append(numero_pregunta_rando)
                    id_pregunta=arreglo_preguntas[numero_pregunta_rando]

                    numero_prueba=q+1
                    arreglo_contenido_pregunta.append(numero_prueba)

                    datos_pregunta=pregunta.objects.filter(id_pregunta=id_pregunta)
                    arreglo_contenido_pregunta.append(datos_pregunta)

                    datos_respuesta=respuesta.objects.filter(id_pregunta=id_pregunta)
                    arreglo_contenido_pregunta.append(datos_respuesta)
                    arreglos_prueba.append(arreglo_contenido_pregunta)
                    q=numero_prueba

                while x < len(arreglos_rando_numeros):
                    if numero_pregunta_rando == arreglos_rando_numeros[x]:
                        x=x+1
                    else:
                        arreglo_contenido_pregunta=[]
                        arreglos_rando_numeros.append(numero_pregunta_rando)
                        id_pregunta=arreglo_preguntas[numero_pregunta_rando]

                        numero_prueba=q+1
                        arreglo_contenido_pregunta.append(numero_prueba)

                        datos_pregunta=pregunta.objects.filter(id_pregunta=id_pregunta)
                        arreglo_contenido_pregunta.append(datos_pregunta)

                        datos_respuesta=respuesta.objects.filter(id_pregunta=id_pregunta)
                        arreglo_contenido_pregunta.append(datos_respuesta)
                        arreglos_prueba.append(arreglo_contenido_pregunta)
                        q=numero_prueba
                        break

            return render(request, 'pruebas/ver_prueba.html',
            {'arreglos_prueba':arreglos_prueba,'pruebs_presona':pruebs_presona,'durancion_pruaba':durancion_pruaba},)

    else:
        message="no tiene permiso para para esta vista"
        return render(request,"inicio/index.html",{'message':message})

@login_required(login_url= '/')
def send_email(request):
    msg=EmailMessage(subject="prueba",from_email="yitmar.14151819@gmail.com",to=['yitmar.14151819@hotmail.com'])
    msg.template_name='pantilla de prueba'
    msg.send()