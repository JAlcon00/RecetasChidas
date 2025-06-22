from typing import List, Optional
from tienda.domain.schemas import UsuarioEntity, CategoriaEntity, ProductoEntity, InventarioEntity
from tienda.persistence.models import Usuario, Categoria, Producto, Inventario


class CategoriaRepositorio:
    """Repositorio básico para la entidad Categoria."""
    @staticmethod
    def obtener_todas() -> List[CategoriaEntity]:
        categorias = Categoria.objects.all()
        return [
            CategoriaEntity(
                id=categoria.id,
                name=categoria.nombre,
                description=categoria.descripcion
            )
            for categoria in categorias
        ]
    
    @staticmethod
    def obtener_por_id(categoria_id: int) -> Optional[CategoriaEntity]:
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            return CategoriaEntity(
                id=categoria.id,
                name=categoria.nombre,
                description=categoria.descripcion
            )
        except Categoria.DoesNotExist:
            return None
        
    @staticmethod
    def crear_categoria(categoriaEntity: CategoriaEntity) -> CategoriaEntity:
        # Crear una nueva categoria
        categoria = Categoria.objects.create(
            nombre=categoriaEntity.name,
            description=categoriaEntity.description
        )
        return CategoriaEntity(
            id=categoria.id,
            name=categoria.nombre,
            description=categoria.descripcion
        )
    
    @staticmethod
    def actualizar_categoria(categoriaEntity: CategoriaEntity) -> CategoriaEntity:
        # Actualizar una categoria existente
        categoria = Categoria.objects.get(id=categoriaEntity.id)
        categoria.nombre = categoriaEntity.name
        categoria.descripcion = categoriaEntity.description
        categoria.save()
        return CategoriaEntity(
            id=categoria.id,
            name=categoria.nombre,
            description=categoria.descripcion
        )
    
    @staticmethod
    def eliminar_categoria(categoria_id: int) -> bool:
        # Eliminar una categoria de la base de datos
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            categoria.delete()
            return True
        except Categoria.DoesNotExist:
            return False

class ProductoRepositorio:
    """Repositorio básico para la entidad Producto."""
    @staticmethod
    def obtener_todos() -> List:
        # Método de ejemplo para obtener todos los productos
        productos = Producto.objects.all()
        return [
            ProductoEntity(
                id=producto.id,
                name=producto.nombre,
                description=producto.descripcion,
                price=producto.precio,
                category=CategoriaEntity(
                    id=producto.categoria.id,
                    name=producto.categoria.nombre,
                    description=producto.categoria.descripcion
                ),
                type=producto.tipo,
                diets=producto.dietas.split(',') if producto.dietas else [],
                flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
                image_url=producto.image_url
            )
            for producto in productos
        ]
    
    @staticmethod
    def obtener_producto_por_id(producto_id: int) -> Optional[ProductoEntity]:
        try:
            producto = Producto.objects.get(id=producto_id)
            return ProductoEntity(
                id=producto.id,
                name=producto.nombre,
                description=producto.descripcion,
                price=producto.precio,
                category=CategoriaEntity(
                    id=producto.categoria.id,
                    name=producto.categoria.nombre,
                    description=producto.categoria.descripcion
                ),
                type=producto.tipo,
                diets=producto.dietas.split(',') if producto.dietas else [],
                flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
                image_url=producto.image_url
            )
        except Producto.DoesNotExist:
            return None
    
    @staticmethod
    def actualizar(producto:ProductoEntity) -> ProductoEntity:
        """Método para actualizar un producto"""
        producto = Producto.objects.get(id=producto.id)
        producto.nombre = producto.name
        producto.descripcion = producto.description

        producto.save()
        return producto

    @staticmethod
    def crear(**kwargs):
        """Método para crear un nuevo producto"""
        producto = Producto.objects.create(**kwargs)
        return producto
    
    @staticmethod
    def eliminar(producto):
        """Método para eliminar un producto"""
        producto.delete()

class InventarioRepositorio:
    @staticmethod
    def obtener_todos() -> List[InventarioEntity]:
        inventarios = Inventario.objects.all()
        return [
            InventarioEntity(
                id=inventario.id,
                product=ProductoEntity(
                    id=inventario.producto.id,
                    name=inventario.producto.nombre,
                    description=inventario.producto.descripcion,
                    price=inventario.producto.precio,
                    category=CategoriaEntity(
                        id=inventario.producto.categoria.id,
                        name=inventario.producto.categoria.nombre,
                        description=inventario.producto.categoria.descripcion
                    ),
                    type=inventario.producto.tipo,
                    diets=inventario.producto.dietas.split(',') if inventario.producto.dietas else [],
                    flavors=inventario.producto.preferencia_sabor.split(',') if inventario.producto.preferencia_sabor else [],
                    image_url=inventario.producto.image_url
                ),
                quantity=inventario.cantidad
            ) for inventario in inventarios
        ]
    
    @staticmethod
    def obtener_por_producto(producto_id: int) -> Optional[InventarioEntity]:
        try:
            inventario = Inventario.objects.get(producto_id=producto_id)
            return InventarioEntity(
                id=inventario.id,
                product=ProductoEntity(
                    id=inventario.producto.id,
                    name=inventario.producto.nombre,
                    description=inventario.producto.descripcion,
                    price=inventario.producto.precio,
                    category=CategoriaEntity(
                        id=inventario.producto.categoria.id,
                        name=inventario.producto.categoria.nombre,
                        description=inventario.producto.categoria.descripcion
                    ),
                    type=inventario.producto.tipo,
                    diets=inventario.producto.dietas.split(',') if inventario.producto.dietas else [],
                    flavors=inventario.producto.preferencia_sabor.split(',') if inventario.producto.preferencia_sabor else [],
                    image_url=inventario.producto.image_url
                ),
                quantity=inventario.cantidad
            )
        except Inventario.DoesNotExist:
            return None

class UsuarioRepositorio:
    """Repositorio básico para la entidad Usuario."""
    def __init__(self):
        pass

    def obtener_todos(self):
        # Método de ejemplo para obtener todos los usuarios
        return []
    
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
    
    @staticmethod
    def actualizar(usuario, **kwargs):
        """Método para actualizar un usuario"""
        for key, value in kwargs.items():
            setattr(usuario, key, value)
        usuario.save()
        return usuario
    
    @staticmethod
    def eliminar(usuario):
        """Método para eliminar un usuario"""
        usuario.delete()
