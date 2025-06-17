from tienda.persistence.repositories import UsuarioRepositorio

class UsuarioService:
    @staticmethod
    def registrar_usuario(nombre, correo_electronico, contrasena, tipo_usuario='cliente'):
        return UsuarioRepositorio.crear(
            nombre=nombre,
            correo_electronico=correo_electronico,
            contrasena=contrasena,
            tipo_usuario=tipo_usuario
        )

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
