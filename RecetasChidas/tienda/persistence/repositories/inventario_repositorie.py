from ..models import Inventario

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
