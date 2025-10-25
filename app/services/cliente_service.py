# /api-clientes-flask/app/services/cliente_service.py

from app import db
from ..models.cliente_model import Cliente
from ..views.cliente_schema import cliente_schema, clientes_schema

class ClienteService:
    
    # Não precisamos mais do __init__ com o banco em memória!

    def create(self, data):
        """
        Cria um novo cliente.
        O Marshmallow (schema.load) faz a validação e cria o objeto Cliente.
        """
        # Deserializa e valida os dados de entrada
        novo_cliente = cliente_schema.load(data)
        
        # Adiciona ao banco de dados
        db.session.add(novo_cliente)
        db.session.commit()
        
        # Serializa e retorna o objeto criado
        return cliente_schema.dump(novo_cliente)
    
    def get_all(self):
        """ Retorna todos os clientes. """
        todos_clientes = Cliente.query.all()
        # Serializa a lista de objetos para JSON
        return clientes_schema.dump(todos_clientes)

    def get_by_id(self, id):
        """ Retorna um cliente pelo ID. """
        cliente = Cliente.query.get(id) # .get() é um atalho para buscar pela Chave Primária
        return cliente_schema.dump(cliente)

    def update(self, id, data):
        """ Atualiza um cliente existente. """
        cliente = Cliente.query.get(id)
        if not cliente:
            return None # Não encontrado

        # Carrega os novos dados no objeto existente (instance=cliente)
        # partial=True permite a atualização parcial (sem enviar todos os campos)
        cliente_atualizado = cliente_schema.load(data, instance=cliente, partial=True)
        
        db.session.commit()
        return cliente_schema.dump(cliente_atualizado)

    def delete(self, id):
        """ Deleta um cliente. """
        cliente = Cliente.query.get(id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            return True
        return False # Não encontrado

    def get_by_name(self, nome):
        """ Busca clientes por nome (case-insensitive). """
        # .ilike() faz uma busca "like" ignorando maiúsculas/minúsculas
        clientes = Cliente.query.filter(Cliente.nome.ilike(f'%{nome}%')).all()
        return clientes_schema.dump(clientes)

    def count(self):
        """ Conta o número total de clientes. """
        return Cliente.query.count()