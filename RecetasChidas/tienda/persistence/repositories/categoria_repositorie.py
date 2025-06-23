from ..models import Categoria
from tienda.domain.schemas import CategoriaEntity
from typing import List, Optional

class CategoriaRepositorio:
    """Repositorio básico para la entidad Categoria."""
    @staticmethod
    def obtener_todas() -> List[CategoriaEntity]:
        categorias = Categoria.objects.all()
        return [
            CategoriaEntity(
                id=categoria.id,
                name=categoria.nombre,
                description=categoria.descripcion
            )
            for categoria in categorias
        ]
    
    @staticmethod
    def obtener_por_id(categoria_id: int) -> Optional[CategoriaEntity]:
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            return CategoriaEntity(
                id=categoria.id,
                name=categoria.nombre,
                description=categoria.descripcion
            )
        except Categoria.DoesNotExist:
            return None
        
    @staticmethod
    def obtener_por_nombre(nombre: str) -> Optional[CategoriaEntity]:
        try:
            categoria = Categoria.objects.get(nombre=nombre)
            return CategoriaEntity(
                id=categoria.id,
                name=categoria.nombre,
                description=categoria.descripcion
            )
        except Categoria.DoesNotExist:
            return None
        
    @staticmethod
    def crear_categoria(categoriaEntity: CategoriaEntity) -> CategoriaEntity:
        # Crear una nueva categoria
        categoria = Categoria.objects.create(
            nombre=categoriaEntity.name,
            descripcion=categoriaEntity.description
        )
        return CategoriaEntity(
            id=categoria.id,
            name=categoria.nombre,
            description=categoria.descripcion
        )
    
    @staticmethod
    def actualizar_categoria(categoriaEntity: CategoriaEntity) -> CategoriaEntity:
        # Actualizar una categoria existente
        categoria = Categoria.objects.get(id=categoriaEntity.id)
        categoria.nombre = categoriaEntity.name
        categoria.descripcion = categoriaEntity.description
        categoria.save()
        return CategoriaEntity(
            id=categoria.id,
            name=categoria.nombre,
            description=categoria.descripcion
        )
    
    @staticmethod
    def eliminar_categoria(categoria_id: int) -> bool:
        # Eliminar una categoria de la base de datos
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            categoria.delete()
            return True
        except Categoria.DoesNotExist:
            return False
