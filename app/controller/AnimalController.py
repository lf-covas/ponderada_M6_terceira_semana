from models.Animal import Animal
import json

caminho_json = "../bd_zoo.json"

class AnimalController:
    @classmethod
    def criar_animal(cls, nome, especie, nome_recinto):

        with open('bd_zoo.json') as arquivo_json:
            dados_json = json.load(arquivo_json)

        recinto_encontrado = False

        for recinto in dados_json['zoo']['recintos']:
            if recinto['nome'] == nome_recinto:
                recinto_encontrado = True
                
                novo_animal = Animal.cria_animal(nome, especie, nome_recinto)
                print(novo_animal)
                animal_info = {
                    'nome': novo_animal.nome,
                    'especie': novo_animal.especie,
                    'nivel_felicidade': novo_animal.nivel_felicidade
                }

                recinto['animais'].append(animal_info)
                recinto['estado'] = cls.verificar_estado_recinto(recinto)

                # break

        if not recinto_encontrado:
            print(f"Recinto '{nome_recinto}' não encontrado. Não é possível criar o animal sem informar um recinto existente.")
            return

        with open('bd_zoo.json', 'w') as arquivo_json:
            json.dump(dados_json, arquivo_json, indent=2)

        return novo_animal, recinto['estado']

    @classmethod
    def verificar_estado_recinto(cls, recinto):
        
        felicidade_media = sum(animal['nivel_felicidade'] for animal in recinto['animais']) / len(recinto['animais'])

        if felicidade_media >= 75:
            estado_recinto = "Muito bem cuidado!"
        elif felicidade_media >= 50:
            estado_recinto = "Bem cuidado!"
        else:
            estado_recinto = "Mal cuidado!"

        print(f"Estado do recinto após adição de animal: {estado_recinto}")
        return estado_recinto
    
    @classmethod
    def alimentar_animal(cls, nome_recinto, nome_animal):
        
        with open('bd_zoo.json') as arquivo_json:
            dados_json = json.load(arquivo_json)

        for recinto in dados_json['zoo']['recintos']:
            if recinto["nome"] == nome_recinto:
                for animal in recinto['animais']:
                    if animal['nome'] == nome_animal: 
                        animal['nivel_felicidade'] += 15
                        break
                break

        recinto['estado'] = cls.verificar_estado_recinto(recinto)

        with open('bd_zoo.json', 'w') as arquivo_json:
            json.dump(dados_json, arquivo_json, indent=2)

        return animal['nivel_felicidade'], recinto['estado']


