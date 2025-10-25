# /api-clientes-flask/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_smorest import Api  # <-- Importa o flask-smorest
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Configuração do Swagger/OpenAPI ---
    app.config["API_TITLE"] = "API de Clientes"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # Onde a doc ficará
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # --- Fim da Configuração ---

    db.init_app(app)
    ma.init_app(app)

    # Inicializa o flask-smorest
    api = Api(app) # <-- Cria a instância da API

    # Registra o Blueprint do Controller NA API
    from .controllers.cliente_controller import cliente_bp
    api.register_blueprint(cliente_bp) # <-- Registra o blueprint na 'api'

    with app.app_context():
        db.create_all()

    return app