import unittest
from controller.AnimalController import AnimalController

class TesteAnimal(unittest.TestCase):
    def test_criar_animal(self):
        animal, estado_recinto = AnimalController.criar_animal("Gabs","Estudante", "Inteli")
        print(animal)
        self.assertEqual(animal.nome, "Gabs")
        self.assertEqual(animal.especie, "Estudante")
        self.assertEqual(animal.recinto, "Inteli")
        self.assertEqual(animal.nivel_felicidade, 0)
        self.assertEqual(estado_recinto, "Vazio")

    def test_alimentar_animal(self):
        nivel_felicidade, estado_recinto = AnimalController.alimentar_animal("Inteli","Yuri")
        self.assertEqual(nivel_felicidade, 90)
        print(estado_recinto)
        self.assertEqual(estado_recinto, "Muito bem cuidado!")

 

    

if __name__ == '__main__':
    unittest.main()
