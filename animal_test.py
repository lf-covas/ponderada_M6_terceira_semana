import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):
    def test_criandoAnimal(self):
        animal = Animal("Yuri", "Resenhador", 40)

        self.assertEqual(animal.nome, "Yuri")
        self.assertEqual(animal.especie, "Resenhador")
        self.assertEqual(animal._nivel_felicidade, 40)

    def test_alimentar_animal(self):
        animal = Animal("Yuri", "Resenhador", 40)
        animal2 = Animal("Yuri", "Resenhador", 99)

        #Adicionando 5 pontos após alimentação
        animal.alimentar_animal()
        self.assertAlmostEqual(animal.nivel_felicidade, 45)

        #Testando nivel maximo de felicidade
        animal2.alimentar_animal()
        self.assertEqual(animal2.nivel_felicidade, 100)

unittest.main()