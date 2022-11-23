from django.shortcuts import render
from django.http import HttpResponseRedirect
from configuracion.views import index

from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import redirect


def error_404(request, exception):
    error_500(request)
    #return HttpResponseRedirect('/')

def error_500(request, exception=None, *_, **_k):
    print('erro6600')
    print(request.path)
    #index(request)
    tx = {
        'path':request.path
    }
    print(tx)
    if request.user.is_authenticated:
            return render(request, 'index.html')
    else:
        response = redirect('/admin')
        return response
    #return render(request, 'index.html')