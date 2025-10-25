# /api-clientes-flask/app/views/cliente_schema.py

from app import ma
from ..models.cliente_model import Cliente

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema para serializar e deserializar os dados do Cliente.
    O load_instance=True transforma o JSON de entrada direto em um
    objeto <Cliente>, que é o que o nosso Service espera.
    """
    class Meta:
        model = Cliente
        load_instance = True # <-- Muito importante!
        # Diz ao Marshmallow para criar um objeto Cliente ao ler um JSON