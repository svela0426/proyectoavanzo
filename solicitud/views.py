from inspect import formatargvalues
import json
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from .forms import SolicitudForm
from .logic.logic_solicitud import create_solicitud


def solicitud_create(request):
    if request.method == 'POST':
        solicitud_dto = create_solicitud(json.loads(request.body))
        solicitud = serializers.serialize('json', [solicitud_dto])
        return HttpResponse(solicitud, content_type='application/json')

def procesar_solicitud(request):
    if request.method == 'POST':
        respuesta = procesar_solicitud(json.loads(request.body))
        return HttpResponse(respuesta)