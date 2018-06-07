
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
"""
def inicio(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# Create your views here.

#@login_required(login_url= '/')
"""
@require_http_methods(["GET","POST"])
class inicio(LoginRequiredMixin):
    def GET(self, request, *args, **kwargs):
        return HttpResponse('holaaaaaaaa')