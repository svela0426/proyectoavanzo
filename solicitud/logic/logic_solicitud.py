from ..models import Solicitud


def create_solicitud(form):
    solicitud = form.save()
    solicitud.save()
    return solicitud