# /api-clientes-flask/app/controllers/cliente_controller.py

from flask import Blueprint, jsonify, request
from ..services.cliente_service import ClienteService

# Cria o Blueprint
cliente_bp = Blueprint('cliente_bp', __name__)

# Instancia o serviço
# (Em uma app maior, usaríamos Injeção de Dependência)
service = ClienteService()

# --- Definição dos Endpoints ---

# CRUD: Create
@cliente_bp.route('/', methods=['POST'])
def create_cliente():
    data = request.json
    try:
        novo_cliente = service.create(data)
        return jsonify(novo_cliente), 201 # 201 Created
    except Exception as e:
        return jsonify({"erro": str(e)}), 400 # 400 Bad Request

# CRUD: Read (Find All)
@cliente_bp.route('/', methods=['GET'])
def get_all_clientes():
    clientes = service.get_all()
    return jsonify(clientes), 200 # 200 OK

# CRUD: Read (Find By ID)
@cliente_bp.route('/<int:id>', methods=['GET'])
def get_cliente_by_id(id):
    cliente = service.get_by_id(id)
    if cliente:
        return jsonify(cliente), 200 # 200 OK
    return jsonify({"erro": "Cliente não encontrado"}), 404 # 404 Not Found

# CRUD: Update
@cliente_bp.route('/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.json
    cliente_atualizado = service.update(id, data)
    if cliente_atualizado:
        return jsonify(cliente_atualizado), 200 # 200 OK
    return jsonify({"erro": "Cliente não encontrado"}), 404 # 404 Not Found

# CRUD: Delete
@cliente_bp.route('/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    if service.delete(id):
        return '', 204 # 204 No Content
    return jsonify({"erro": "Cliente não encontrado"}), 404 # 404 Not Found

# Requisito Específico: Find By Name
@cliente_bp.route('/buscar', methods=['GET'])
def find_cliente_by_name():
    # Pega o nome da query string (ex: /clientes/buscar?nome=Joao)
    nome = request.args.get('nome')
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400
        
    clientes = service.get_by_name(nome)
    return jsonify(clientes), 200 # 200 OK

# Requisito Específico: Contagem
@cliente_bp.route('/contagem', methods=['GET'])
def count_clientes():
    total = service.count()
    return jsonify({"total": total}), 200 # 200 OK