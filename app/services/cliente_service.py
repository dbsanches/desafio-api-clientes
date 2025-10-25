# /api-clientes-flask/app/services/cliente_service.py

# (Na Fase 2, esta classe importará o Model)
# from ..models.cliente_model import Cliente
# from .. import db

class ClienteService:
    
    # --- Início da Fase 1: Persistência em Memória ---
    def __init__(self):
        # Simulação de um banco de dados em memória
        self.clientes_db = {
            1: {"id": 1, "nome": "Cliente Exemplo 1", "email": "c1@email.com", "telefone": "11999990001"},
            2: {"id": 2, "nome": "Cliente Exemplo 2", "email": "c2@email.com", "telefone": "11999990002"}
        }
        self.next_id = 3 # Próximo ID a ser usado
    
    def _validar_cliente(self, data):
        """Valida os dados de entrada."""
        if 'nome' not in data or not data['nome']:
            raise Exception("O campo 'nome' é obrigatório.")
        if 'email' not in data or not data['email']:
            raise Exception("O campo 'email' é obrigatório.")
        
        # Valida email único
        email = data['email']
        if any(c['email'] == email for c in self.clientes_db.values()):
            raise Exception("Este email já está cadastrado.")

    def create(self, data):
        self._validar_cliente(data)
        
        novo_cliente = {
            "id": self.next_id,
            "nome": data['nome'],
            "email": data['email'],
            "telefone": data.get('telefone') # .get() permite valor opcional
        }
        self.clientes_db[self.next_id] = novo_cliente
        self.next_id += 1
        return novo_cliente
    
    def get_all(self):
        return list(self.clientes_db.values())

    def get_by_id(self, id):
        return self.clientes_db.get(id) # Retorna None se não achar

    def update(self, id, data):
        if id not in self.clientes_db:
            return None # Não encontrado

        # Valida email único (se o email estiver sendo alterado)
        if 'email' in data and data['email'] != self.clientes_db[id]['email']:
             if any(c['email'] == data['email'] for c in self.clientes_db.values()):
                raise Exception("Este email já está cadastado por outro usuário.")

        cliente = self.clientes_db[id]
        cliente['nome'] = data.get('nome', cliente['nome'])
        cliente['email'] = data.get('email', cliente['email'])
        cliente['telefone'] = data.get('telefone', cliente['telefone'])
        
        self.clientes_db[id] = cliente
        return cliente

    def delete(self, id):
        if id in self.clientes_db:
            del self.clientes_db[id]
            return True
        return False # Não encontrado

    def get_by_name(self, nome):
        # Busca case-insensitive
        return [c for c in self.clientes_db.values() if nome.lower() in c['nome'].lower()]

    def count(self):
        return len(self.clientes_db)
    # --- Fim da Fase 1 ---