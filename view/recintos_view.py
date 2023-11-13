from flask import Blueprint, request, jsonify
from repository.recinto_repository import recinto_repository

recinto_blueprint = Blueprint('recinto', __name__)

@recinto_blueprint.route('/cria_recinto', methods = ['POST'])
def cria_recinto():
    dados = request.get_json()
    recinto = recinto_repository.cria_recinto(dados['nome'], dados['capacidade'])

    return jsonify({'mensagem': 'Recinto criado com sucesso!', 'recinto': recinto.obterJson()})

@recinto_blueprint.route('/recintos', methods = ['GET'])
def obtem_recintos():
    recintos = []
    for i in recinto_repository.obter_recintos():
        recintos.append(i.obterJson())

    print('oiii', recintos)
    return jsonify({'recintos': recintos})