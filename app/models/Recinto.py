class Recinto:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []

    def verifica_estado_recinto(self):
        if not self.animais:
            return "Vazio"
        
        felicidade_media = sum(animal.nivel_felicidade for animal in self.animais) / len(self.animais)

        if felicidade_media >= 75:
            estado_recinto = "Muito bem cuidado!"
        elif felicidade_media >= 50:
            estado_recinto = "Bem cuidado!"
        else:
            estado_recinto = "Mal cuidado!"

        print(f"Estado do recinto após adição de animal: {estado_recinto}")
        return estado_recinto
