from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from . import views

urlpatterns = [
    path('solicitudcreate/', csrf_exempt(views.solicitud_create), name='solicitudcreate'),
]