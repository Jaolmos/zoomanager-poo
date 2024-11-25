from typing import Optional
from .animal import Animal

class Bird(Animal):
    """Clase que representa a un ave."""
    
    def __init__(self, name: str, species: str, wingspan: float):
        super().__init__(name, species)
        self._wingspan = wingspan
    
    @property
    def wingspan(self) -> float:
        return self._wingspan
    
    def make_sound(self) -> str:
        return "¡Pío pío!"
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nEnvergadura de alas: {self._wingspan}m" 