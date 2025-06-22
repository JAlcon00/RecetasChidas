from tienda.persistence.repositories import ProductoRepositorio
from tienda.domain.schemas import ProductoEntity

class ProductoService:
    def __init__(self, repository=None):
        self.repository = repository or ProductoRepositorio
        pass

    def obtener_productos(self):
        productos = self.repository.obtener_todos()
        return productos
    
    def obtener_producto_por_id(self, producto_id):
        return self.repository.obtener_producto_por_id(producto_id)
    
    def crear_producto(self, nombre:str, descripcion:str, precio:float, categoria:str, tipo:str, dietas, preferencia_sabor, imagen_url):
        categoriaEntity = self.repository.obtener_categoria_por_nombre(categoria)
        productoEntity = ProductoEntity.create(
            name=nombre,
            description=descripcion,
            price=precio,
            category=categoriaEntity,
            type=tipo,
            diets=dietas.split(',') if dietas else [],
            flavors=preferencia_sabor.split(',') if preferencia_sabor else [],
            image_url=imagen_url
        )
        return self.repository.crearProducto(productoEntity)
    
    def actualizar_producto(self, producto_id, nombre, descripcion, precio, categoria, tipo, dietas, preferencia_sabor, imagen_url):
        productoEntity = self.repository.obtener_producto_por_id(producto_id)
        if not productoEntity:
            return None
        categoriaEntity = self.repository.obtener_categoria_por_nombre(categoria)
        productoEntity.name = nombre
        productoEntity.description = descripcion
        productoEntity.price = precio
        productoEntity.category = categoriaEntity
        productoEntity.type = tipo
        productoEntity.diets = dietas.split(',') if dietas else []
        productoEntity.flavors = preferencia_sabor.split(',') if preferencia_sabor else []
        productoEntity.image_url = imagen_url
        return self.repository.actualizar(productoEntity)
    
    def eliminar_producto(self, producto_id):
        return self.repository.eliminar(producto_id)

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
    def actualizar_producto(producto, **kwargs):
        return ProductoRepositorio.actualizar(producto, **kwargs)

    @staticmethod
    def eliminar_producto(producto):
        ProductoRepositorio.eliminar(producto)
