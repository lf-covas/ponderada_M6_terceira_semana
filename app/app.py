from flask import Flask, request, jsonify
from controller.AnimalController import AnimalController
from controller.RecintoController import RecintoController
import json
caminho_json = "../bd_zoo.json"

app = Flask(__name__)
animal_controller = AnimalController()

@app.route('/criar_animal', methods=['POST'])
def criar_animal():
    dados = request.get_json()

    nome = dados.get('nome')
    especie = dados.get('especie')
    nome_recinto = dados.get('recinto')

    AnimalController.criar_animal(nome=nome, especie=especie, nome_recinto=nome_recinto)
    return jsonify({'mensagem': f'Animal {nome} da espécie {especie} criado com sucesso!'})

@app.route('/criar_recinto', methods = ['POST'])
def criar_recinto():
    dados = request.get_json()

    nome = dados.get('nome')

    RecintoController.criar_recinto(nome = nome)
    return jsonify({'mensagem': f'Recinto {nome} criado com sucesso!'})

@app.route('/alimentar_animal', methods = ['POST'])
def alimentar_animal():
    dados = request.get_json()

    nome_recinto = dados.get('nome_recinto')
    nome_animal = dados.get('nome_animal')

    AnimalController.alimentar_animal(nome_recinto = nome_recinto, nome_animal = nome_animal)

    return jsonify({'mensagem': f'Animal {nome_animal} do recinto {nome_recinto} alimentado com sucesso!'})

@app.route('/recebe_visitas', methods = ['POST'])
def adicionar_visitas():
    with open('bd_zoo.json', 'r') as arquivo_json:
        dados_json = json.load(arquivo_json)

        soma = 0

        for recinto in dados_json['zoo']['recintos']:
            for animal in recinto['animais']:
                soma += animal['nivel_felicidade']

        if soma >= 500:
            dados_json['zoo']['visitas'] += 2
            mensagem = 'Visitas adicionadas com sucesso!'
        elif soma >= 1000:
            dados_json['zoo']['visitas'] += 4
            mensagem = 'Visitas adicionadas com sucesso!'
        else:
            mensagem = 'Sem condições de receber visitas'

    with open('bd_zoo.json', 'w') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=2)

    return jsonify({'mensagem': mensagem})

if __name__ == '__main__':
    app.run(debug=True)

