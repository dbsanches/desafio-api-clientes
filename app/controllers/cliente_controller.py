# /api-clientes-flask/app/controllers/cliente_controller.py

from flask import Blueprint, jsonify, request
from ..services.cliente_service import ClienteService
from marshmallow import ValidationError  # Importa o erro de validação

cliente_bp = Blueprint('cliente_bp', __name__)
service = ClienteService()

# --- Definição dos Endpoints ---

@cliente_bp.route('/', methods=['POST'])
def create_cliente():
    data = request.json
    try:
        # Service agora usa Marshmallow, que pode levantar ValidationError
        novo_cliente = service.create(data)
        return jsonify(novo_cliente), 201 # 201 Created
    except ValidationError as e:
        # Se a validação falhar, retorna os erros
        return jsonify({"erro": "Dados inválidos", "mensagens": e.messages}), 400
    except Exception as e:
        # Pega outros erros (ex: email duplicado do banco)
        return jsonify({"erro": str(e)}), 400 # 400 Bad Request

# GET All (Não muda)
@cliente_bp.route('/', methods=['GET'])
def get_all_clientes():
    clientes = service.get_all()
    return jsonify(clientes), 200 # 200 OK

# GET By ID (Não muda)
@cliente_bp.route('/<int:id>', methods=['GET'])
def get_cliente_by_id(id):
    cliente = service.get_by_id(id)
    if cliente:
        return jsonify(cliente), 200 # 200 OK
    return jsonify({"erro": "Cliente não encontrado"}), 404 # 404 Not Found

# UPDATE
@cliente_bp.route('/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.json
    try:
        cliente_atualizado = service.update(id, data)
        if cliente_atualizado:
            return jsonify(cliente_atualizado), 200 # 200 OK
        return jsonify({"erro": "Cliente não encontrado"}), 404 # 404 Not Found
    except ValidationError as e:
        return jsonify({"erro": "Dados inválidos", "mensagens": e.messages}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 400 # 400 Bad Request

# DELETE (Não muda)
@cliente_bp.route('/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    if service.delete(id):
        return '', 204 # 204 No Content
    return jsonify({"erro": "Cliente não encontrado"}), 404 # 404 Not Found

# Find By Name (Não muda)
@cliente_bp.route('/buscar', methods=['GET'])
def find_cliente_by_name():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400
        
    clientes = service.get_by_name(nome)
    return jsonify(clientes), 200 # 200 OK

# Count (Não muda)
@cliente_bp.route('/contagem', methods=['GET'])
def count_clientes():
    total = service.count()
    return jsonify({"total": total}), 200 # 200 OK