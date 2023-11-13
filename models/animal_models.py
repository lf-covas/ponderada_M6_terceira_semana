class Animal():
    def __init__(self, nome, especie, nivel_felicidade, recinto):
        print("Novo animal criado")
        self.nome = nome
        self.especie = especie
        self._nivel_felicidade = nivel_felicidade
        self.recinto = recinto

    @property
    def nivel_felicidade(self):
        return self._nivel_felicidade
    
    @nivel_felicidade.setter
    def nivel_felicidade(self, valor):
        self._nivel_felicidade = max(0, min(valor,100))

    def alimentar_animal(self):
        self._nivel_felicidade += 5

    def obterJson(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "nivel_felicidade": self.nivel_felicidade
        }