from typing import Optional
from ..models import Usuario
from tienda.domain.schemas import UsuarioEntity

class UsuarioRepositorio:
    @staticmethod
    def obtener_por_id(usuario_id: int) -> Optional[UsuarioEntity]:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            return UsuarioEntity(
                id=usuario.id,
                nombre=usuario.nombre,
                correo_electronico=usuario.correo_electronico,
                contrasena='',
                tipo_usuario=usuario.tipo_usuario
            )
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def buscar_por_email_y_password(email, password):
        try:
            user = Usuario.objects.get(correo_electronico=email)
            if user.contrasena == password:
                return UsuarioEntity(
                    id=user.id,
                    nombre=user.nombre,
                    correo_electronico=user.correo_electronico,
                    contrasena='',
                    tipo_usuario=user.tipo_usuario
                )
        except Usuario.DoesNotExist:
            return None
        return None
