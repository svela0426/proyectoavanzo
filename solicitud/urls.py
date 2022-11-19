from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from . import views

urlpatterns = [
    path('solicitudes/', views.solicitud_list, name='solicitudList'),
    path('solicitudes1/', views.solicitud_list1, name='solicitudList'),
    path('solicitudview/', views.solicitudes_view, name='solicitudView'),
    path('solicitudcreate/', csrf_exempt(views.solicitud_create), name='solicitudcreate'),
    path('solicitudprocesar/', csrf_exempt(views.solicitud_procesar), name='solicitudprocesar'),

]