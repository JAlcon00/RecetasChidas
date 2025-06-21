from dataclasses import dataclass
from typing import Optional, List

@dataclass
class UsuarioEntity:
    id: Optional[int]
    nombre: str
    correo_electronico: str
    contrasena: str
    tipo_usuario: str  # 'cliente' o 'administrador'

@dataclass
class CategoriaEntity:
    id: Optional[int]
    name: str
    description: str

@dataclass
class ProductoEntity:
    id: Optional[int]
    name: str
    description: str
    price: float
    category: CategoriaEntity
    type: str  # 'comida preparada' o 'kit'
    diets: List[str]  # Ejemplo: ['vegana', 'sin gluten']
    flavors: List[str]  # Ejemplo: ['picante', 'dulce']
    image_url: str

@dataclass
class Inventario:
    id: Optional[int]
    product: ProductoEntity
    quantity: int

