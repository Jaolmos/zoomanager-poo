from typing import Optional
from .animal import Animal

class Mammal(Animal):
    """Clase que representa a un mamífero."""
    
    def __init__(self, name: str, species: str, legs: int):
        super().__init__(name, species)
        self._legs = legs
    
    @property
    def legs(self) -> int:
        return self._legs
    
    def make_sound(self) -> str:
        return "¡Sonido genérico de mamífero!"
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nNúmero de patas: {self._legs}" 