from abc import ABC, abstractmethod
from typing import Optional

class Animal(ABC):
    """Clase base abstracta para todos los animales."""
    
    def __init__(self, name: str, species: str):
        self._name = name
        self._species = species
        
    @property
    def name(self) -> str:
        return self._name
        
    @property
    def species(self) -> str:
        return self._species
    
    @abstractmethod
    def make_sound(self) -> str:
        """Método abstracto que debe ser implementado por las clases hijas."""
        pass
    
    def __str__(self) -> str:
        return f"Nombre: {self._name}\nEspecie: {self._species}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}', species='{self._species}')" 