from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clientes/', views.cliente_list),
    path('clientecreate/', csrf_exempt(views.cliente_create), name='clientecreate'),
]