from flask import Flask, request, jsonify
from animal import Animal
from recinto import Recinto
import json

with open('bd_zoo.json', 'r') as arquivo_json:
    bd_zoo = json.load(arquivo_json)

app = Flask('Zoo')
NovoRecinto = Recinto()
NovoAnimal = Animal()

@app.route('/criar_animal', methods=['POST'])
def criar_animal():
    data = request.json

    if 'nome' in data and 'especie' in data and 'nivel_felicidade' in data:
        nome = data['nome']
        especie = data['especie']
        nivel_felicidade = data['nivel_felicidade']
        novoAnimal = Animal(nome, especie, nivel_felicidade)
        bd_zoo['animais'].append(novoAnimal)
        return jsonify({'message': 'Animal criado com sucesso'})

    return jsonify({'error': 'Dados inválidos'}), 400

@app.route('/alimentar_animal/<int:animal_id>', methods = ['POST', 'PUT'])
def alimentar_animal(animal_id):
    animal = next((bixo for bixo in bd_zoo['animais'] if bixo['id'] == animal_id), None)

    if animal:
        animal_obj = Animal(
            nome=animal['nome'],
            especie=animal['especie'],
            nivel_felicidade=animal['_nivel_felicidade']
        )

        animal_obj.alimentar_animal()
        animal['_nivel_felicidade'] = animal_obj.nivel_felicidade
    
        return jsonify({'message': 'Animal alimentado com sucesso'})
    else:
        return jsonify({'error': 'Animal não encontrado'}, 404)

@app.route('/criar_recinto', methods = ['POST'])
def criar_recinto():
    data = request.json

    if 'nome' in data and 'condicao' in data and 'capacidade' in data:
        nome = data['nome']
        condicao = data['condicao']
        capacidade = data['capacidade']
        lista_animais = data.get('animais',[])
        novoRecinto = Recinto(nome, condicao, capacidade, lista_animais)
        bd_zoo['recintos'].append(novoRecinto)

        for animal_id in lista_animais:
                    animal = next((a for a in bd_zoo['animais'] if a['id'] == animal_id), None)
                    if animal:
                        animal['recinto_id'] = novoRecinto['id']

        return jsonify({'message': 'Recinto criado com sucesso'})

    return jsonify({'error': 'Dados inválidos'}), 400

@app.route('/adicionar_animal_ao_recinto/<int:recinto_id>/<int:animal_id>', methods=['POST'])
def adicionar_animal_ao_recinto(recinto_id, animal_id):
    recinto = next((local for local in bd_zoo['recintos'] if local['id'] == recinto_id), None)
    
    if recinto:
        animal = next((bixo for bixo in bd_zoo['animais'] if bixo['id'] == animal_id), None)
        
        if animal:
            recinto_obj = Recinto(
                nome=recinto['nome'],
                condicao=recinto['condicao'],
                capacidade=recinto['capacidade'],
                animais=recinto.get('animais', [])
            )
            recinto_obj.add_animal(animal_id)
            recinto['animais'] = recinto_obj.animais
            return jsonify({'message': 'Animal adicionado ao recinto com sucesso'})
        else:
            return jsonify({'error': 'Animal não encontrado'}, 404)
    else:
        return jsonify({'error': 'Recinto não encontrado'}, 404)

app.run()