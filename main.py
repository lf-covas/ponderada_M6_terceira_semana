from flask import Flask, request
from animal import Animal
from recinto import Recinto
import bd_zoo
import json

app = Flask('Zoo')
NovoRecinto = Recinto()
NovoAnimal = Animal()

zoo = Zoo()

@app.route('/zoo_do_covas', methods = ['POST'])
def criaZoo():

    data = bd_zoo
    data = request.get.json()

    if 'recintos' in data:
        for recinto in data['recintos']:
            enclosure_name = recinto.get('nome_recinto')
            enclosure_condition = recinto.get('condicao_recinto')
            enclosure_capacity = recinto.get('capacidade_recinto')
            enclosure_vist = recinto.get('visitas_recinto')
            enclosure_animals = recinto.get('animais')

            NovoRecinto(enclosure_name, enclosure_condition, enclosure_capacity, enclosure_vist, enclosure_animals)
            zoo.adicionar_recinto(NovoRecinto)

    if 'animais' in data:
        for animal in data['animais']:
            animal_name = animal.get('nome_animal')
            animal_species = animal.get('especie_animal')
            NovoAnimal(animal_name, animal_species)

    if 'visita_zoo' in data:
        for visitas_zoo in data['visitas']:
            quantidade = visitas_zoo.get('quantidade')
            zoo.add_visitantes(quantidade)

    def add_visitante(self, visitas):
        self.enclosure_vist = self.enclosure_vist + visitas 

    return "Zoo criado"
    

app.run()