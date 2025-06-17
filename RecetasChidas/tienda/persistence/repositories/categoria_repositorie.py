from ..models import Categoria

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
