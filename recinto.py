class Recinto():
    def __init__(self, nome, condicao, capacidade, animais=[]):
        print("Novo recinto criado")
        self.nome = nome
        self.condicao = condicao
        self._capacidade = capacidade
        self.animais = animais

    @property
    def capacidade(self):
        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, valor):
        self._capacidade = max(0, min(valor, 10))

    def add_animal(self, animal):
        self.animais.append(animal)