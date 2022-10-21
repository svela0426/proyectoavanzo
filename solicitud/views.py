from inspect import formatargvalues
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SolicitudForm
from .logic.logic_solicitud import create_solicitud


def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = create_solicitud(form)
            return HttpResponse(solicitud, status=200)