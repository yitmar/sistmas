from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, DetailView
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from apps.resultados.models import resultado
from django.core.mail import EmailMessage

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

class crear_prueba(CreateView):
    template_name=('pruebas/crear_pruebas.html')
    model=Prueba
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
    queryset=Prueba.objects.all()
    def get_context_data(self, **kwargs):
        context= super(lista_prueba, self).get_context_data(**kwargs)
        return context
"""
class datos(CreateView):
    template_name=('pruebas/ver_prueba.html')
    model= Prueba
    success_url=('/')
    form_class=formulario_realizar_prueba
"""
@require_http_methods(["GET", "POST"])
def datos(request,pk):
    
    prueba=Prueba.objects.filter(id_prueba=pk)
    arreglo_pregunta=[]
    for item in prueba:
        id_participante=item.id_participante
        id_dificultad=item.id_dificultad
        id_categoria=item.id_categoria
        cantidad_pregunta=item.cantidad_pregunta
        arreglo_preguntas=item.arreglo_preguntas
        q=0
        while q > len(arreglo_preguntas):
            arreglo_pregunta.append(arreglo_preguntas[q])
        a=arreglo_preguntas[0]
        b=0
        while b<cantidad_pregunta:
            b=b+1
        a=1

    cantidad=cantidad_pregunta    
    numero_preguntas=pregunta.objects.filter(id_pregunta=a)

    for item in numero_preguntas:
        nombre=item.nombre_pregunta
        tipo_pregunta=item.tipo_pregunta
    respuestas=respuesta.objects.filter(id_pregunta=a)

    for item in respuestas:
        id_respuesta=item.id_respuesta
        nombre_respuesta=item.nombre_respuesta
        tipo_respuesta=item.tipo_respuesta
  
    if request.method == 'POST':
        a=0
        nota_evaluacion=0
        nota=0
        arreglo_respuesta=[]
        while a < cantidad:
            b=request.POST['respuesta']
            arreglo_respuesta.append(b)
            consulta_nota=respuesta.objects.filter(id_respuesta=b)
            for consulta_de in consulta_nota:
                if(consulta_de.tipo_respuesta):
                    nota=1
            nota_evaluacion=nota+nota_evaluacion  
            a=a+1
        nueva_prueba=resultado(id_participante=id_participante,id_categoria=id_categoria,arreglo_preguntas=arreglo_pregunta,arreglo_respuesta=arreglo_respuesta,nota_evaluacion=nota_evaluacion)
        nueva_prueba.save()
        send_email(request)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'pruebas/ver_prueba.html',
        {'numero_preguntas':numero_preguntas,'respuestas':respuestas,'prueba':prueba},)

def send_email(request):
    
    msg=EmailMessage(subject="prueba",from_email="yitmar.14151819@gmail.com",to=['yitmar.14151819@hotmail.com'])
    msg.template_name='pantilla de prueba'
    msg.send()
