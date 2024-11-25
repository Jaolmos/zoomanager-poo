🦁 ZooManager POO 🦅
Aplicación de gestión de zoológico desarrollada en Python utilizando programación orientada a objetos.

📋 Características
Gestión de animales (mamíferos y aves)
Búsqueda y listado de animales
Interfaz por menú interactivo
Sistema de validación de duplicados

🚀 Estructura

zoomanager/
├── models/
│   ├── animal.py    # Clase base
│   ├── mammal.py    # Mamíferos
│   ├── bird.py      # Aves
│   └── zoo.py       # Gestión principal
├── utils/
│   ├── exceptions.py
│   └── menu.py
└── tests/
    └── test_animal.py

💻 Uso
El menú principal ofrece las siguientes opciones:

1. Agregar un nuevo animal
2. Buscar un animal por nombre
3. Listar todos los animales
4. Salir

🧪 Tests
Los tests verifican:
Creación de animales
Adición al zoológico
Prevención de duplicados
Sonidos de animales

Para ejecutar:
python -m unittest tests/test_animal.py

👥 Autor
Tu Nombre - @tu-usuario