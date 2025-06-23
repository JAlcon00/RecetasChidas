from tienda.persistence.repositories import InventarioRepositorio, ProductoRepositorio
from tienda.domain.schemas import InventarioEntity

class InventarioService:
    def __init__(self, repository=None):
        self.repository = repository or InventarioRepositorio()

    def obtener_inventarios(self):
        return self.repository.obtener_todos()
    
    def obtener_inventario_por_producto(self, producto_id):
        return self.repository.obtener_por_producto(producto_id)
        
    def registrar_inventario(self, productoId, cantidad):
        productoEntity = ProductoRepositorio.obtener_producto_por_id(productoId)
        inventarioEntity = InventarioEntity.create(product=productoEntity, quantity=cantidad)
        return self.repository.crearInventario(inventarioEntity)
    
    def actualizar_inventario(self, producto_id, cantidad):
        inventarioEntity = self.repository.obtener_por_producto(producto_id)
        if not inventarioEntity:
            return None
        inventarioEntity.quantity = cantidad
        return self.repository.actualizarInventario(inventarioEntity)
    
    def eliminar_inventario(self, inventario_id):
        return self.repository.eliminarInventario(inventario_id)

    @staticmethod
    def obtener_inventario_por_id(inventario_id):
        return InventarioRepositorio.obtener_por_id(inventario_id)

    @staticmethod
    def eliminar_inventario(inventario):
        InventarioRepositorio.eliminar(inventario)
