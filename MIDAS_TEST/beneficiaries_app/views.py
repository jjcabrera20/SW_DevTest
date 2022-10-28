from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#from .forms import PersonaForm
#from .models import Persona, PersonXML
#import dicttoxml


def index(request):
    return render(request, 'wellcome.html')
