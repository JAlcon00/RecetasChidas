from tienda.persistence.repositories import InventarioRepositorio

class InventarioService:
    @staticmethod
    def registrar_inventario(producto, cantidad):
        return InventarioRepositorio.crear(
            producto=producto,
            cantidad=cantidad
        )

    @staticmethod
    def obtener_inventarios():
        return InventarioRepositorio.obtener_todos()

    @staticmethod
    def obtener_inventario_por_id(inventario_id):
        return InventarioRepositorio.obtener_por_id(inventario_id)

    @staticmethod
    def actualizar_inventario(inventario, **kwargs):
        return InventarioRepositorio.actualizar(inventario, **kwargs)

    @staticmethod
    def eliminar_inventario(inventario):
        InventarioRepositorio.eliminar(inventario)
