import unittest
from controller.RecintoController import RecintoController
from models.Recinto import Recinto

class TesteRecinto(unittest.TestCase):
    def test_criar_recinto(self):
        recinto = RecintoController.criar_recinto("FSA")
        self.assertEqual(recinto.nome, "FSA")
        self.assertEqual(recinto.animais, [])
        self.assertEqual(recinto.verifica_estado_recinto(), "Vazio")

if __name__ == '__main__':
    unittest.main()