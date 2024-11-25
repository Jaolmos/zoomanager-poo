class Menu:
    """Clase para manejar la interfaz de menú del programa."""
    
    @staticmethod
    def show_main_menu() -> str:
        """Muestra el menú principal y retorna la opción seleccionada."""
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar animal")
        print("2. Listar animales")
        print("3. Buscar animal")
        print("4. Salir")
        
        while True:
            option = input("\nSeleccione una opción (1-4): ")
            if option in ["1", "2", "3", "4"]:
                return option
            print("Opción inválida. Intente nuevamente.")
    
    @staticmethod
    def show_animal_creation_menu() -> str:
        """Muestra el menú de creación de animales y retorna la opción seleccionada."""
        print("\n=== TIPO DE ANIMAL ===")
        print("1. Mamífero")
        print("2. Ave")
        
        while True:
            option = input("\nSeleccione el tipo de animal (1-2): ")
            if option in ["1", "2"]:
                return option
            print("Opción inválida. Intente nuevamente.") 