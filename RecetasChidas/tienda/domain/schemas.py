from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Usuario:
    id: Optional[int]
    nombre: str
    correo_electronico: str
    contrasena: str
    tipo_usuario: str  # 'cliente' o 'administrador'

@dataclass
class Categoria:
    id: Optional[int]
    name: str
    description: str

@dataclass
class Producto:
    id: Optional[int]
    name: str
    description: str
    price: float
    category: Categoria
    type: str  # 'comida preparada' o 'kit'
    diets: List[str]  # Ejemplo: ['vegana', 'sin gluten']
    flavors: List[str]  # Ejemplo: ['picante', 'dulce']

@dataclass
class Inventario:
    id: Optional[int]
    product: Producto
    quantity: int

