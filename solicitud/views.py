from inspect import formatargvalues
import json
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from .forms import SolicitudForm
from .logic.logic_solicitud import create_solicitud, process_solicitud, get_solicitudes
from django.contrib.auth.decorators import login_required
from proyectoavanzo.auth0backend import getRole

@login_required
def solicitud_create(request):
    role = getRole(request)
    if role == "Cliente":
        if request.method == 'POST':
            solicitud_dto = create_solicitud(json.loads(request.body))
            solicitud = serializers.serialize('json', [solicitud_dto])
            return HttpResponse(solicitud, content_type='application/json')

@login_required
def solicitud_procesar(request):
    if request.method == 'POST':
        respuesta = process_solicitud(json.loads(request.body))
        return HttpResponse(respuesta)


@login_required
def solicitud_list(request):
    role = getRole(request)
    if role == "Cliente":
        solicitudes = get_solicitudes()
        return render(request, 'cliente.html')
    else:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return render(request, 'error.html')


def solicitud_list1(request):
    #role = getRole(request)
    #if role == "Cliente":
        solicitudes = get_solicitudes()
        return HttpResponse(serializers.serialize('json', solicitudes), content_type='application/json')
    #else:
        #messages.error(request, 'No tienes permisos para acceder a esta página')
        #return HttpResponseRedirect(reverse('home'))

