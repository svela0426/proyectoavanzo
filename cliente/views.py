from django.shortcuts import HttpResponse, render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_cliente import create_cliente

# Create your views here.

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        cliente = create_cliente(form)
        data = form.cleaned_data
        return HttpResponse(data, status=200)
        