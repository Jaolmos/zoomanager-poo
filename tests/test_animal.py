import unittest
from models.mammal import Mammal
from models.bird import Bird
from models.zoo import Zoo
from utils.exceptions import AnimalException

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo("Zoo de Prueba")
        self.mammal = Mammal("León", "Panthera leo", 4)
        self.bird = Bird("Águila", "Aquila chrysaetos", 2.3)
    
    def test_animal_creation(self):
        self.assertEqual(self.mammal.name, "León")
        self.assertEqual(self.bird.name, "Águila")
    
    def test_zoo_add_animal(self):
        self.zoo.add_animal(self.mammal)
        self.assertEqual(self.zoo.find_animal("León"), self.mammal)
    
    def test_duplicate_animal(self):
        self.zoo.add_animal(self.mammal)
        with self.assertRaises(AnimalException):
            self.zoo.add_animal(Mammal("León", "Panthera leo", 4))
    
    def test_animal_sounds(self):
        self.assertIsInstance(self.mammal.make_sound(), str)
        self.assertIsInstance(self.bird.make_sound(), str)

if __name__ == '__main__':
    unittest.main() 