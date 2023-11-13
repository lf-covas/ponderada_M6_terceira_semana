from models.animal_models import Animal

class AnimalRepository():
    animais = []
    def criar_animal(self, nome, especie, nivel_felicidade, recinto):
        novo_animal = Animal(nome, especie, nivel_felicidade, recinto)
        self.animais.append(novo_animal)

        return novo_animal
    
    def obter_animais(self):
        animais_info = [{'nome': animal.nome, 'especie': animal.especie, 'nivel_felicidade': animal.nivel_felicidade} for animal in self.animais]

        return animais_info
    
    def obter_animal_por_nome(self, nome_animal):
        for animal in self.animais:
            if animal.nome == nome_animal:
                return animal
    
animal_repository = AnimalRepository()