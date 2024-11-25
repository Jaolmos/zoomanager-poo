from typing import List, Optional
from .animal import Animal
from utils.exceptions import AnimalException

class Zoo:
    """Clase que representa un zoológico."""
    
    def __init__(self, name: str):
        self._name = name
        self._animals: List[Animal] = []
    
    @property
    def name(self) -> str:
        return self._name
    
    def add_animal(self, animal: Animal) -> None:
        """Añade un animal al zoológico."""
        if any(a.name == animal.name for a in self._animals):
            raise AnimalException(f"Ya existe un animal con el nombre {animal.name}")
        self._animals.append(animal)
    
    def find_animal(self, name: str) -> Optional[Animal]:
        """Busca un animal por su nombre."""
        return next((animal for animal in self._animals if animal.name == name), None)
    
    def list_animals(self) -> None:
        """Lista todos los animales en el zoológico."""
        if not self._animals:
            print("No hay animales en el zoológico.")
            return
        
        for animal in self._animals:
            print(f"\n{animal}")
            print(f"Sonido: {animal.make_sound()}") 