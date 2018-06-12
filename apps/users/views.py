from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import participante
from .forms import participante_form
from django.utils import timezone
# Create your views here.
#@login_required(login_url= '/')
"""
class registro(CreateView):
    template_name='users/registro.html'    
    model= participante
    success_url=('/users')
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
def post_new(request):
        form = PostForm()
        return render(request, 'users/registro.html', {'form': form}) 
        """