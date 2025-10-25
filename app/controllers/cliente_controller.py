# /api-clientes-flask/app/controllers/cliente_controller.py

from flask import request, jsonify
from flask_smorest import Blueprint, abort # <-- MUDANÇA
from ..services.cliente_service import ClienteService
from ..views.cliente_schema import ClienteSchema # <-- Importa o Schema
from marshmallow import ValidationError

# MUDANÇA: O Blueprint agora é do flask_smorest
# O primeiro argumento 'clientes' é o NOME do "Tag" no Swagger UI
cliente_bp = Blueprint("clientes", __name__, description="Operações de Clientes")
service = ClienteService()


@cliente_bp.route('/', methods=['POST'])
@cliente_bp.arguments(ClienteSchema) # <-- MÁGICA 1: Lê o JSON, valida, e cria um objeto Cliente
@cliente_bp.response(201, ClienteSchema) # <-- MÁGICA 2: Pega o objeto retornado e transforma em JSON
def create_cliente(novo_cliente): # <-- MUDANÇA: Recebe o objeto do decorator @arguments
    """ Cria um novo cliente. """
    try:
        # MUDANÇA: O service agora recebe o OBJETO direto
        cliente = service.create(novo_cliente)
        return cliente
    except Exception as e:
        # Pega erros (ex: email duplicado do banco)
        abort(400, message=f"Erro ao criar cliente: {str(e)}")


@cliente_bp.route('/', methods=['GET'])
@cliente_bp.response(200, ClienteSchema(many=True)) # <-- MÁGICA: Sabe que é uma LISTA de clientes
def get_all_clientes():
    """ Retorna uma lista de todos os clientes. """
    return service.get_all()


@cliente_bp.route('/<int:id>', methods=['GET'])
@cliente_bp.response(200, ClienteSchema) # <-- MÁGICA: Sabe que é UM cliente
def get_cliente_by_id(id):
    """ Retorna um cliente específico pelo seu ID. """
    cliente = service.get_by_id(id)
    if not cliente:
        abort(404, message="Cliente não encontrado.")
    return cliente


@cliente_bp.route('/<int:id>', methods=['PUT'])
@cliente_bp.arguments(ClienteSchema) # <-- MÁGICA: Valida o JSON de entrada
@cliente_bp.response(200, ClienteSchema) # <-- MÁGICA: Retorna o cliente atualizado
def update_cliente(data_update, id): # <-- MUDANÇA: 'data_update' vem do @arguments
    """ Atualiza um cliente existente (substituição completa). """
    try:
        # MUDANÇA: O 'data_update' do Marshmallow é um dicionário (pois load_instance=True não foi usado no 'arguments')
        # Para ser mais simples, vamos manter o service esperando um dicionário para updates
        cliente_atualizado = service.update(id, data_update)
        if not cliente_atualizado:
            abort(404, message="Cliente não encontrado.")
        return cliente_atualizado
    except ValidationError as e:
        abort(400, message=f"Dados inválidos: {e.messages}")
    except Exception as e:
        abort(400, message=f"Erro ao atualizar: {str(e)}")


@cliente_bp.route('/<int:id>', methods=['DELETE'])
@cliente_bp.response(204) # <-- MÁGICA: Documenta que a resposta é 204 (sem conteúdo)
def delete_cliente(id):
    """ Deleta um cliente pelo seu ID. """
    if not service.delete(id):
        abort(404, message="Cliente não encontrado.")
    return '' # Retorna vazio, como esperado pelo 204


@cliente_bp.route('/buscar', methods=['GET'])
@cliente_bp.response(200, ClienteSchema(many=True))
def find_cliente_by_name():
    """ Busca clientes por parte do nome (query param 'nome'). """
    nome = request.args.get('nome')
    if not nome:
        abort(400, message="Parâmetro 'nome' é obrigatório.")
    return service.get_by_name(nome)


@cliente_bp.route('/contagem', methods=['GET'])
def count_clientes():
    """ Retorna a contagem total de clientes. """
    total = service.count()
    return jsonify({"total": total}) # (Endpoint simples pode ficar como está)