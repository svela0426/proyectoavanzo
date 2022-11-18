from ..models import Solicitud
import time, random, sched
import queue as q
import threading

queue = q.Queue()


def create_solicitud(form):
    solicitud = Solicitud(
        cliente=form["cliente"],
        monto=form["monto"],
        cuotas=form["cuotas"],
        estado=form["estado"]
    )
    solicitud.save()
    return solicitud


def worker():
    while True:
        item = queue.get()
        if item is not None:
            start = time.time()
            print("Procesando solicitud:",item.id)
            tiempo_secs = random.randint(20,30)
            if tiempo_secs%3 == 0:
                item.estado = "Rechazada"
            else:
                item.estado = "Aprobada"
            print("Estado:",item.estado)
            end = time.time()
            print("Procesada en:",end-start, "s")
        else:
            print("No hay solicitudes en la cola")
            time.sleep(3)
        queue.task_done()

def process_solicitud(form):
    solicitud = Solicitud(
        cliente=form["cliente"],
        monto=form["monto"],
        cuotas=form["cuotas"],
        estado=form["estado"]
    )
    
    queue.put(solicitud)


    solicitud.save()
    return solicitud

def get_solicitudes():
    solicitudes = Solicitud.objects.all()
    return solicitudes

def start_worker():
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()


