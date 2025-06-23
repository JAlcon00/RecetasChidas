from typing import List, Optional
from tienda.domain.schemas import InventarioEntity, ProductoEntity, CategoriaEntity
from ..models import Inventario

class InventarioRepositorio:
    @staticmethod
    def obtener_todos() -> List[InventarioEntity]:
        inventarios = Inventario.objects.all()
        return [
            InventarioEntity(
                id=inventario.id,
                product=ProductoEntity(
                    id=inventario.producto.id,
                    name=inventario.producto.nombre,
                    description=inventario.producto.descripcion,
                    price=inventario.producto.precio,
                    category=CategoriaEntity(
                        id=inventario.producto.categoria.id,
                        name=inventario.producto.categoria.nombre,
                        description=inventario.producto.categoria.descripcion
                    ),
                    type=inventario.producto.tipo,
                    diets=inventario.producto.dietas.split(',') if inventario.producto.dietas else [],
                    flavors=inventario.producto.preferencia_sabor.split(',') if inventario.producto.preferencia_sabor else [],
                    image_url=inventario.producto.image_url
                ),
                quantity=inventario.cantidad
            ) for inventario in inventarios
        ]
    
    @staticmethod
    def obtener_por_producto(producto_id: int) -> Optional[InventarioEntity]:
        try:
            inventario = Inventario.objects.get(producto_id=producto_id)
            return InventarioEntity(
                id=inventario.id,
                product=ProductoEntity(
                    id=inventario.producto.id,
                    name=inventario.producto.nombre,
                    description=inventario.producto.descripcion,
                    price=inventario.producto.precio,
                    category=CategoriaEntity(
                        id=inventario.producto.categoria.id,
                        name=inventario.producto.categoria.nombre,
                        description=inventario.producto.categoria.descripcion
                    ),
                    type=inventario.producto.tipo,
                    diets=inventario.producto.dietas.split(',') if inventario.producto.dietas else [],
                    flavors=inventario.producto.preferencia_sabor.split(',') if inventario.producto.preferencia_sabor else [],
                    image_url=inventario.producto.image_url
                ),
                quantity=inventario.cantidad
            )
        except Inventario.DoesNotExist:
            return None
        
    @staticmethod
    def crearInventario(inventarioEntity: InventarioEntity) -> InventarioEntity:
        inventario = Inventario(
            producto_id=inventarioEntity.product.id,
            cantidad=inventarioEntity.quantity
        )
        inventario.save()
        return inventarioEntity
    
    @staticmethod
    def actualizarInventario(inventarioEntity: InventarioEntity) -> InventarioEntity:
        # Actualizar un inventario existente
        inventario = Inventario.objects.get(id=inventarioEntity.id)
        inventario.producto_id = inventarioEntity.product.id
        inventario.cantidad = inventarioEntity.quantity
        inventario.save()
        return InventarioEntity(
            id=inventario.id,
            product=ProductoEntity(
                id=inventario.producto.id,
                name=inventario.producto.nombre,
                description=inventario.producto.descripcion,
                price=inventario.producto.precio,
                category=CategoriaEntity(
                    id=inventario.producto.categoria.id,
                    name=inventario.producto.categoria.nombre,
                    description=inventario.producto.categoria.descripcion
                ),
                type=inventario.producto.tipo,
                diets=inventario.producto.dietas.split(',') if inventario.producto.dietas else [],
                flavors=inventario.producto.preferencia_sabor.split(',') if inventario.producto.preferencia_sabor else [],
                image_url=inventario.producto.image_url
            ),
            quantity=inventario.cantidad
        )
    
    @staticmethod
    def eliminarInventario(inventarioId: int) -> bool:
        # Eliminar un inventario de la base de datos
        try:
            inventario = Inventario.objects.get(id=inventarioId)
            inventario.delete()
            return True
        except Inventario.DoesNotExist:
            return False