class Animal:
    def __init__(self, nome, especie, recinto, nivel_felicidade=50):
        self.nome = nome
        self.especie = especie
        self.recinto = recinto
        self.nivel_felicidade = nivel_felicidade

    @classmethod
    def cria_animal(cls, nome, especie, recinto):
        novo_animal = cls(nome, especie, recinto, nivel_felicidade=50)
        return novo_animal
    
