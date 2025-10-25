# /api-clientes-flask/app/__init__.py

from flask import Flask

def create_app():
    """
    Factory function para criar a instância da aplicação Flask.
    """
    app = Flask(__name__)

    # (Futuramente, carregaremos as configs do app/config/settings.py)
    # app.config.from_object('app.config.settings.Config')
    
    # (Futuramente, inicializaremos o DB e o Marshmallow aqui)
    # db.init_app(app)
    # ma.init_app(app)

    # Registra o Blueprint do Controller
    from .controllers.cliente_controller import cliente_bp
    
    # Define o prefixo /clientes para todas as rotas do controller
    app.register_blueprint(cliente_bp, url_prefix='/clientes')

    return app