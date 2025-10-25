# /api-clientes-flask/app/services/cliente_service.py

from app import db
from ..models.cliente_model import Cliente
# Removemos a importação dos schemas, o service não precisa mais deles
# from ..views.cliente_schema import cliente_schema, clientes_schema

class ClienteService:

    def create(self, novo_cliente: Cliente): # <-- MUDANÇA: Recebe o objeto Cliente
        """
        Cria um novo cliente.
        """
        # A validação e deserialização JÁ FORAM FEITAS pelo controller
        
        # Apenas adicionamos o objeto recebido
        db.session.add(novo_cliente)
        db.session.commit()
        
        return novo_cliente # Retorna o objeto
    
    def get_all(self):
        return Cliente.query.all() # <-- MUDANÇA: Retorna a lista de OBJETOS

    def get_by_id(self, id):
        return Cliente.query.get(id) # <-- MUDANÇA: Retorna o OBJETO ou None

    def update(self, id, data_update: dict): # <-- MUDANÇA: Renomeado para clareza
        """ Atualiza um cliente existente. """
        cliente = Cliente.query.get(id)
        if not cliente:
            return None

        # Atualiza os campos do objeto 'cliente' com os dados do dicionário
        # (Aqui mantemos o dicionário 'data' por ser mais fácil para update parcial)
        if 'nome' in data_update:
            cliente.nome = data_update['nome']
        if 'email' in data_update:
            # (Aqui poderíamos adicionar a validação de email duplicado)
            cliente.email = data_update['email']
        if 'telefone' in data_update:
            cliente.telefone = data_update['telefone']
        
        db.session.commit()
        return cliente # Retorna o objeto atualizado

    def delete(self, id):
        cliente = Cliente.query.get(id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            return True
        return False

    def get_by_name(self, nome):
        return Cliente.query.filter(Cliente.nome.ilike(f'%{nome}%')).all() # <-- MUDANÇA: Retorna OBJETOS

    def count(self):
        return Cliente.query.count() # (Sem mudança)