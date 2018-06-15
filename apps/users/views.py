from django.shortcuts import render,redirect
from django.views.generic import CreateView, DetailView
from .models import participante
from .forms import participante_form

# Create your views here.
#@login_required(login_url= '/')

class registro(CreateView):
    template_name='users/registro.html'    
    model= participante
    form_class=participante_form
    success_url=('/')
    def model_valid(self, form):
        super(registro, self).form_valid(form)
        return redirect(r'')
    def model_invalid(self, form):
        return super(registro, self).form_invalid(form)   
"""
def registro(request):
    form=participante_form(request.POST)
    if form.is_valid():
        pos= form.save(commit=False)
        pos.fecha_participacion= timezone.now()
        pos.save()
        return redirect('/')
    else:
        form=participante_form()
    return render(request,'users/registro.html',{'form':form})
"""