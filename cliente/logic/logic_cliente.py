from ..models import Cliente

def create_cliente(form):
    cliente = Cliente(
        name=form['name']
    )
    cliente.save()
    return cliente