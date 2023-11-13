class Recinto:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.animais = []
        self.estado = "Bem Cuidado"

    def addAnimal(self, animal):
        self.animais.append(animal)

    def obterJson(self):
        animaisJson = []
        for i in self.animais:
            animaisJson.append(i.obterJson())

        return {
            "nome": self.nome,
            "capacidade": self.capacidade,
            "animais": animaisJson,
            "estado": self.estado
        }

