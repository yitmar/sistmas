
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import datetime
import templates

"""
def inicio(request):
    now = datetime.datetime.now()
    html = "<html><body> aunq sea la ora %s.</body></html>" % now
    return HttpResponse(html)

# Create your views here.

#@login_required(login_url= '/')
"""

class inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'inicio/index.html')