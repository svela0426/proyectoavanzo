from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SolicitudForm
from .logic.logic_solicitud import get_solicitudes, create_solicitud

def solicitud_list(request):
    solicitudes = get_solicitudes()
    context = { 'solicitudes': solicitudes }
    return render(request, 'solicitud/solicitud.html', context)

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            create_solicitud(form)
            messages.success(request, 'Solicitud creada exitosamente')
            return HttpResponseRedirect(reverse('solicitudCreate'))
        else:
            print(form.errors)
    else:
        form = SolicitudForm()
    context = { 'form': form }
    return render(request, 'solicitud/solicitudCreate.html', context)
