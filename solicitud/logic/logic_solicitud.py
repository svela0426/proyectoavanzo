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
    tiempo_secs = random.randint(120,180)
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(tiempo_secs, 1, solicitud.save)
    return solicitud