from models.recinto_models import Recinto

class RecintoRepository():
    recintos = []

    def cria_recinto(self, nome, capacidade):
        novo_recinto = Recinto(nome, capacidade)
        self.recintos.append(novo_recinto)
        return novo_recinto
    
    def obter_recinto(self, nome):
        for recinto in self.recintos:
            if recinto.nome == nome:
                return recinto
        return None
    
    def obter_recintos(self):
        return self.recintos
    
recinto_repository = RecintoRepository()