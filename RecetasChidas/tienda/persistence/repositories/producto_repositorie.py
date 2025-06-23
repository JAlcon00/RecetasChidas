from typing import List, Optional
from ..models import Producto, Categoria
from tienda.domain.schemas import ProductoEntity, CategoriaEntity

class ProductoRepositorio:
    """Repositorio básico para la entidad Producto."""
    @staticmethod
    def obtener_todos() -> List[ProductoEntity]:
        # Método de ejemplo para obtener todos los productos
        productos = Producto.objects.all()
        return [
            ProductoEntity(
                id=producto.id,
                name=producto.nombre,
                description=producto.descripcion,
                price=producto.precio,
                category=CategoriaEntity(
                    id=producto.categoria.id,
                    name=producto.categoria.nombre,
                    description=producto.categoria.descripcion
                ),
                type=producto.tipo,
                diets=producto.dietas.split(',') if producto.dietas else [],
                flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
                image_url=producto.image_url
            )
            for producto in productos
        ]
    
    @staticmethod
    def obtener_producto_por_id(producto_id: int) -> Optional[ProductoEntity]:
        try:
            producto = Producto.objects.get(id=producto_id)
            return ProductoEntity(
                id=producto.id,
                name=producto.nombre,
                description=producto.descripcion,
                price=producto.precio,
                category=CategoriaEntity(
                    id=producto.categoria.id,
                    name=producto.categoria.nombre,
                    description=producto.categoria.descripcion
                ),
                type=producto.tipo,
                diets=producto.dietas.split(',') if producto.dietas else [],
                flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
                image_url=producto.image_url
            )
        except Producto.DoesNotExist:
            return None
    
    @staticmethod
    def actualizar(productoEntity:ProductoEntity) -> ProductoEntity:
        """Método para actualizar un producto"""
        producto = Producto.objects.get(id=productoEntity.id)
        producto.nombre = productoEntity.name
        producto.descripcion = productoEntity.description
        producto.precio = productoEntity.price
        producto.categoria = Categoria.objects.get(id=productoEntity.category.id)
        producto.tipo = productoEntity.type
        producto.dietas = ','.join(productoEntity.diets) if productoEntity.diets else ''
        producto.preferencia_sabor = ','.join(productoEntity.flavors) if productoEntity.flavors else ''
        producto.image_url = productoEntity.image_url
        producto.save()
        return ProductoEntity(
            id=producto.id,
            name=producto.nombre,
            description=producto.descripcion,
            price=producto.precio,
            category=CategoriaEntity(
                id=producto.categoria.id,
                name=producto.categoria.nombre,
                description=producto.categoria.descripcion
            ),
            type=producto.tipo,
            diets=producto.dietas.split(',') if producto.dietas else [],
            flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
            image_url=producto.image_url
        )

    @staticmethod
    def crearProducto(productoEntity: ProductoEntity) -> ProductoEntity:
        # Crear un nuevo producto
        producto = Producto.objects.create(
            nombre=productoEntity.name,
            descripcion=productoEntity.description,
            precio=productoEntity.price,
            categoria=Categoria.objects.get(id=productoEntity.category.id),
            tipo=productoEntity.type,
            dietas=','.join(productoEntity.diets) if productoEntity.diets else '',
            preferencia_sabor=','.join(productoEntity.flavors) if productoEntity.flavors else '',
            image_url=productoEntity.image_url
        )
        return ProductoEntity(
            id=producto.id,
            name=producto.nombre,
            description=producto.descripcion,
            price=producto.precio,
            category=CategoriaEntity(
                id=producto.categoria.id,
                name=producto.categoria.nombre,
                description=producto.categoria.descripcion
            ),
            type=producto.tipo,
            diets=producto.dietas.split(',') if producto.dietas else [],
            flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
            image_url=producto.image_url
        )
    
    @staticmethod
    def eliminar(productoId: int) -> bool:
        # Eliminar una nota de la base de datos
        try:
            producto = Producto.objects.get(id=productoId)
            producto.delete()
            return True
        except Producto.DoesNotExist:
            return False