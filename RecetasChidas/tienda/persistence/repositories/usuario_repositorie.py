from ..models import Usuario

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
