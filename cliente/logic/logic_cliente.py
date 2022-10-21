from ..models import Cliente

def create_cliente(form):
    cliente = form.save()
    cliente.save()
    return cliente