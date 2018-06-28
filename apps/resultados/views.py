from django.shortcuts import render
from django.views.generic import View

# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'resultados/index.html')