from django.shortcuts import HttpResponse, render

# Create your views here.
def homepage_view(request):
    return HttpResponse('Hola mundo')