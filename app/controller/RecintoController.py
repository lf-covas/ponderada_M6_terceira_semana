from models.Recinto import Recinto

import json

caminho_json = 'bd_zoo.json'

class RecintoController:
    @classmethod
    def criar_recinto(cls, nome):
        novo_recinto = Recinto(nome)

        recinto = {
            'nome': novo_recinto.nome,
            'animais': [],
            'estado': novo_recinto.verifica_estado_recinto()
        }

        with open('bd_zoo.json', "r") as arquivo_json:
            dados_json = json.load(arquivo_json)


        dados_json['zoo']['recintos'].append(recinto)
        print(dados_json)

        with open('bd_zoo.json', 'w') as arquivo_json:
            json.dump(dados_json, arquivo_json, indent=2)

        return novo_recinto

