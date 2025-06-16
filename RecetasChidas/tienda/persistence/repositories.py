from .models import Categoria, Usuario, Producto, Inventario

class CategoriaRepositorio:
    @staticmethod
    def obtener_todas():
        return Categoria.objects.all()

    @staticmethod
    def obtener_por_id(categoria_id):
        return Categoria.objects.filter(id=categoria_id).first()

    @staticmethod
    def crear(**kwargs):
        return Categoria.objects.create(**kwargs)

    @staticmethod
    def actualizar(categoria, **kwargs):
        for clave, valor in kwargs.items():
            setattr(categoria, clave, valor)
        categoria.save()
        return categoria

    @staticmethod
    def eliminar(categoria):
        categoria.delete()

class UsuarioRepositorio:
    @staticmethod
    def obtener_todos():
        return Usuario.objects.all()

    @staticmethod
    def obtener_por_id(usuario_id):
        return Usuario.objects.filter(id=usuario_id).first()

    @staticmethod
    def crear(**kwargs):
        return Usuario.objects.create(**kwargs)

    @staticmethod
    def actualizar(usuario, **kwargs):
        for clave, valor in kwargs.items():
            setattr(usuario, clave, valor)
        usuario.save()
        return usuario

    @staticmethod
    def eliminar(usuario):
        usuario.delete()

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

class InventarioRepositorio:
    @staticmethod
    def obtener_todos():
        return Inventario.objects.all()

    @staticmethod
    def obtener_por_id(inventario_id):
        return Inventario.objects.filter(id=inventario_id).first()

    @staticmethod
    def crear(**kwargs):
        return Inventario.objects.create(**kwargs)

    @staticmethod
    def actualizar(inventario, **kwargs):
        for clave, valor in kwargs.items():
            setattr(inventario, clave, valor)
        inventario.save()
        return inventario

    @staticmethod
    def eliminar(inventario):
        inventario.delete()
