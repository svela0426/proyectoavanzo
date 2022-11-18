from ..models import Solicitud
import time, random, sched

def create_solicitud(form):
    solicitud = Solicitud(
        cliente=form["cliente"],
        monto=form["monto"],
        cuotas=form["cuotas"],
        estado=form["estado"]
    )
    solicitud.save()
    return solicitud

def process_solicitud(form):
    solicitud = Solicitud(
        cliente=form["cliente"],
        monto=form["monto"],
        cuotas=form["cuotas"],
        estado=form["estado"]
    )
    
    tiempo_secs = random.randint(20,30)
    print("Sleep:",tiempo_secs)
    time.sleep(tiempo_secs)
    if tiempo_secs%3 == 0:
        solicitud.estado = "Rechazada"
    else:
        solicitud.estado = "Aprobada"
    print("Estado:",solicitud.estado)
    print("Procesada en:",tiempo_secs)
    solicitud.save()
    return solicitud

def get_solicitudes():
    solicitudes = Solicitud.objects.all()
    return solicitudes