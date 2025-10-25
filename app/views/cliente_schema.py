# /api-clientes-flask/app/views/cliente_schema.py

from app import ma  # Importa a instância 'ma' do __init__.py
from ..models.cliente_model import Cliente

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    """
    Este Schema usa o 'AutoSchema' para automaticamente
    criar os campos de serialização com base no 'ClienteModel'.
    """
    class Meta:
        model = Cliente
        load_instance = True # Permite carregar dados direto para o objeto Cliente
        include_fk = True  # (Se tivéssemos chaves estrangeiras)

# Instancia os schemas para usarmos no nosso código
# Um para serializar/deserializar UM cliente
cliente_schema = ClienteSchema()
# Um para serializar/deserializar UMA LISTA de clientes
clientes_schema = ClienteSchema(many=True)