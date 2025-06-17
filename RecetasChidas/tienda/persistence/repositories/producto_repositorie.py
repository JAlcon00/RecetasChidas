from ..models import Producto

class ProductoRepositorio:
    @staticmethod
    def obtener_todos():
        return Producto.objects.all()

    @staticmethod
    def obtener_por_id(producto_id):
        return Producto.objects.filter(id=producto_id).first()

    @staticmethod
    def crear(**kwargs):
        return Producto.objects.create(**kwargs)

    @staticmethod
    def actualizar(producto, **kwargs):
        for clave, valor in kwargs.items():
            setattr(producto, clave, valor)
        producto.save()
        return producto

    @staticmethod
    def eliminar(producto):
        producto.delete()
