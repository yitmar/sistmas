from django.shortcuts import render
from django.views.generic import View, ListView

 
# Create your views here.
#@login_required(login_url= '/')

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'inicio/index.html')