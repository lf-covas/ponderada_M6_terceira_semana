import unittest

class Recinto():
    def __init__(self, nome, condicao, capacidade, visitas):
        print("Novo recinto criado")
        self.nome = nome
        self.condicao = condicao
        self._capacidade = capacidade
        self.visitas = visitas
        self.animais = []

    @property
    def capacidade(self):
        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, valor):
        self._capacidade = max(0, min(valor, 10))

    def add_animal(self, animal):
        self.animais.append(animal)