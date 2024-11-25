from typing import List, Optional
from models.animal import Animal
from models.mammal import Mammal
from models.bird import Bird
from models.zoo import Zoo
from utils.menu import Menu
from utils.exceptions import AnimalException

def main():
    menu = Menu()
    zoo = Zoo("Mi Zoológico")
    
    while True:
        try:
            option = menu.show_main_menu()
            
            if option == "1":
                animal_type = menu.show_animal_creation_menu()
                if animal_type == "1":
                    name = input("Nombre del mamífero: ")
                    species = input("Especie: ")
                    legs = int(input("Número de patas: "))
                    zoo.add_animal(Mammal(name, species, legs))
                elif animal_type == "2":
                    name = input("Nombre del ave: ")
                    species = input("Especie: ")
                    wingspan = float(input("Envergadura de alas (metros): "))
                    zoo.add_animal(Bird(name, species, wingspan))
                
            elif option == "2":
                print("\nAnimales en el zoológico:")
                zoo.list_animals()
                
            elif option == "3":
                name = input("Nombre del animal a buscar: ")
                animal = zoo.find_animal(name)
                if animal:
                    print(f"\nInformación del animal:\n{animal}")
                else:
                    print("\nAnimal no encontrado.")
                    
            elif option == "4":
                print("\n¡Hasta luego!")
                break
                
        except AnimalException as e:
            print(f"\nError: {e}")
        except ValueError as e:
            print("\nError: Valor inválido ingresado.")
        except Exception as e:
            print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main() 