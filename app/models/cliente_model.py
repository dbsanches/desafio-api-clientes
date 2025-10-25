# /api-clientes-flask/app/models/cliente_model.py

from app import db  # Importa a instância 'db' do __init__.py

class Cliente(db.Model):
    # __tablename__ = 'clientes'  # (Opcional) Nome da tabela no DB
    
    # Define as colunas da nossa tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Cliente {self.nome}>'