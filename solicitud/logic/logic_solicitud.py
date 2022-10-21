from ..models import Solicitud


def create_solicitud(form):
    solicitud = Solicitud(
        cliente=form['cliente'],
        fecha=form['fecha'],
        monto=form['monto'],
        cuotas=form['cuotas'],
        estado=form['estado']
    )
    solicitud.save()
    return solicitud