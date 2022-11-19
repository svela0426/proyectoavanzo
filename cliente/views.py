import json
from django.shortcuts import HttpResponse, render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render

from .logic.logic_cliente import create_cliente

# Create your views here.
def cliente_create(request):
    if request.method == 'POST':
        cliente_dto = create_cliente(json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto])
        return render(request, 'cliente.html')