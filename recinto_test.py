import unittest
from recinto import Recinto
from animal import Animal

class TestRecinto(unittest.TestCase):
    def test_criandoRecinto(self):
        recinto = Recinto('Resenhadores', 'Boa', 10, 0)

        self.assertEqual(recinto.nome, 'Resenhadores')
        self.assertEqual(recinto.condicao, 'Boa')
        self.assertEqual(recinto._capacidade, 10)
        self.assertEqual(recinto.animais, [])


    def test_addAnimal(self):
        recinto = Recinto('Resenhadores', 'Boa', 10, 0)

        animal = Animal('Rafael', 'Brinca muito', 80)

        recinto.add_animal(animal)

        self.assertIn(animal, recinto.animais)

unittest.main()