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

    @classmethod
    def create(cls, name: str, description: str):
        # Crea una instancia de la entidad CategoriaEntity
        return cls(id=None, name=name, description=description)

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
class InventarioEntity:
    id: Optional[int]
    product: ProductoEntity
    quantity: int

    @classmethod
    def create(cls, product: ProductoEntity, quantity: int):
        # Crea una instancia de la entidad InventarioEntity
        return cls(id=None, product=product, quantity=quantity)

