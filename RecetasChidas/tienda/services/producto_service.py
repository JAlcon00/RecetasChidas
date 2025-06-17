from tienda.persistence.repositories import ProductoRepositorio

class ProductoService:
    @staticmethod
    def registrar_producto(nombre, descripcion, precio, categoria, tipo, dietas='', preferencia_sabor='', imagen_url='https://example.com/default.jpg'):
        return ProductoRepositorio.crear(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            tipo=tipo,
            dietas=dietas,
            preferencia_sabor=preferencia_sabor,
            imagen_url=imagen_url
        )

    @staticmethod
    def obtener_productos():
        return ProductoRepositorio.obtener_todos()

    @staticmethod
    def obtener_producto_por_id(producto_id):
        return ProductoRepositorio.obtener_por_id(producto_id)

    @staticmethod
    def actualizar_producto(producto, **kwargs):
        return ProductoRepositorio.actualizar(producto, **kwargs)

    @staticmethod
    def eliminar_producto(producto):
        ProductoRepositorio.eliminar(producto)
