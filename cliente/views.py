from django.shortcuts import HttpResponse, render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_cliente import get_clientes, create_cliente

# Create your views here.
def cliente_list(request):
    clientes = get_clientes()
    context = {'clientes_list': clientes}
    return render(request, 'cliente/cliente_list.html', context)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'Cliente creado correctamente')
            return HttpResponseRedirect(reverse('clienteCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()
    
    context = {'form': form}

    return render(request, 'cliente/cliente_create.html', context)