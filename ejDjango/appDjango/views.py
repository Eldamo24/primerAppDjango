from django.shortcuts import render
from appDjango.models import Familiar
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiares(request):
    familiar = Familiar.objects.all()
    return render(request, "listaFamiliares.html", {"familia": familiar})
    

