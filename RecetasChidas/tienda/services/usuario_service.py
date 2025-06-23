from tienda.persistence.repositories.usuario_repositorie import UsuarioRepositorio

class UsuarioService:
    def __init__(self, repository=None):
        self.repository = repository or UsuarioRepositorio

    def buscar_usuario(self, email, password):
        usuario = self.repository.buscar_por_email_y_password(email, password)
        if usuario:
            return {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "correo_electronico": usuario.correo_electronico,
                "tipo_usuario": usuario.tipo_usuario
            }
        return None

    @staticmethod
    def obtener_usuarios():
        return UsuarioRepositorio.obtener_todos()

    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        return UsuarioRepositorio.obtener_por_id(usuario_id)

    @staticmethod
    def actualizar_usuario(usuario, **kwargs):
        return UsuarioRepositorio.actualizar(usuario, **kwargs)

    @staticmethod
    def eliminar_usuario(usuario):
        UsuarioRepositorio.eliminar(usuario)
