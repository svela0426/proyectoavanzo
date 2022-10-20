from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VariableForm
from .logic.variable_logic import get_variables, create_variable

def variable_list(request):
    variables = get_variables()
    context = {'variables_list': variables}
    return render(request, 'variable/variables.html', context)

def variable_create(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            create_variable(form)
            messages.success(request, 'Variable creada exitosamente')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = VariableForm()

    context = {'variables_list': variables}

    return render(request, 'variable/variable_create.html', context)