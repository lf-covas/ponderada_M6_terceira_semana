from flask import Blueprint, request, jsonify
from models.animal_models import Animal
from repository.animal_repository import animal_repository
from repository.recinto_repository import recinto_repository

animal_blueprint = Blueprint('animal', __name__)

@animal_blueprint.route('/cria_animal', methods=['POST'])
def cria_animal():
    dados = request.get_json()

    if(not dados['recinto']):
        return jsonify({
            'mensagem': 'precisa do nome de um recinto assim recinto.nome'
        })
    
    recinto = recinto_repository.obter_recinto(dados['recinto'])
    if(not recinto):
         return jsonify({
            'mensagem': 'Recinto não encontrado'
        })
    
    
    novo_animal = animal_repository.criar_animal(dados['nome'], dados['especie'], dados['nivel_felicidade'], recinto)
    return jsonify({'mensagem': 'Animal criado com sucesso!', 'animal': {'nome': novo_animal.nome, 'especie': novo_animal.especie, 'nivel_felicidade': novo_animal.nivel_felicidade}})

@animal_blueprint.route('/animais', methods=['GET'])
def obtem_animais():
    animais = []
    for i in recinto_repository.obter_recintos():
        animais.append(i.obterJson())

    return jsonify({'animais': animais})


@animal_blueprint.route('/alimenta_animal', methods = ['POST'])
def alimentar_animal():
    dados = request.get_json()

    if 'nome' not in dados:
        return jsonify({'mensagem': 'O campo "nome" é obrigatório'})
    
    nome_animal = dados['nome']

    animal = animal_repository.obter_animal_por_nome(nome_animal)

    animal.alimentar_animal()