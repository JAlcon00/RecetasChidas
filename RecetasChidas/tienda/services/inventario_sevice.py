from tienda.persistence.repositories import InventarioRepositorio

class InventarioService:
    def __init__(self, repository=None):
        self.repository = repository or InventarioRepositorio()

    def obtener_inventarios(self):
        return self.repository.obtener_todos()
    
    def obtener_inventario_por_producto(self, producto_id):
        return self.repository.obtener_por_producto(producto_id)
        
    def registrar_inventario(producto, cantidad):
        return InventarioRepositorio.crear(
            producto=producto,
            cantidad=cantidad
        )

    @staticmethod
    def obtener_inventario_por_id(inventario_id):
        return InventarioRepositorio.obtener_por_id(inventario_id)

    @staticmethod
    def actualizar_inventario(inventario, **kwargs):
        return InventarioRepositorio.actualizar(inventario, **kwargs)

    @staticmethod
    def eliminar_inventario(inventario):
        InventarioRepositorio.eliminar(inventario)
