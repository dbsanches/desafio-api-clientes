# /api-clientes-flask/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Inicializa as extensões (ainda sem app)
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """
    Factory function para criar a instância da aplicação Flask.
    """
    app = Flask(__name__)
    
    # Define o caminho base do projeto
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # Configuração do Banco de Dados
    # 'sqlite:///database.db' significa:
    # Use o driver sqlite, e o arquivo 'database.db'
    # ficará na raiz do projeto (no mesmo nível de run.py)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Associa as extensões à instância da aplicação
    db.init_app(app)
    ma.init_app(app)

    # Registra o Blueprint do Controller
    from .controllers.cliente_controller import cliente_bp
    app.register_blueprint(cliente_bp, url_prefix='/clientes')

    # --- Cria o arquivo do banco de dados (se não existir) ---
    with app.app_context():
        # Este comando cria todas as tabelas definidas nos seus Models
        db.create_all()

    return app