from tienda.domain.schemas import ProductoEntity, CategoriaEntity
from tienda.persistence.repositories.producto_repositorie import ProductoRepositorio
from tienda.persistence.repositories.categoria_repositorie import CategoriaRepositorio

categoriaRepositorio = CategoriaRepositorio()

class ProductoService:
    def __init__(self, repository=None):
        self.repository = repository or ProductoRepositorio
        pass

    def validar_producto(self, nombre:str, descripcion:str, precio:float, categoria:CategoriaEntity, tipo:str,imagen_url:str):
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacio")
        if not descripcion:
            raise ValueError("La descripcion del producto no puede estar vacia")
        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor a cero")
        if not categoria:
            raise ValueError("La categoria del producto no puede estar vacia")
        if not tipo:
            raise ValueError("El tipo del producto no puede estar vacio")
        if not imagen_url:
            raise ValueError("La URL de la imagen del producto no puede estar vacia")

    def obtener_productos(self):
        productos = self.repository.obtener_todos()
        return productos
    
    def obtener_producto_por_id(self, producto_id):
        return self.repository.obtener_producto_por_id(producto_id)
    
    def crear_producto(self, nombre:str, descripcion:str, precio:float, categoria:CategoriaEntity, tipo:str, dietas:str, preferencia_sabor:str, imagen_url):
        self.validar_producto(nombre, descripcion, precio, categoria, tipo, imagen_url)
        productoEntity = ProductoEntity.create(
            name=nombre,
            description=descripcion,
            price=precio,
            category=categoria,
            type=tipo,
            diets=dietas.split(',') if dietas else [],
            flavors=preferencia_sabor.split(',') if preferencia_sabor else [],
            image_url=imagen_url
        )
        return self.repository.crearProducto(productoEntity)
    
    def actualizar_producto(self, producto_id, nombre, descripcion, precio, categoria, tipo, dietas, preferencia_sabor, imagen_url):
        self.validar_producto(nombre, descripcion, precio, categoria, tipo, imagen_url)
        productoEntity = self.repository.obtener_producto_por_id(producto_id)
        if not productoEntity:
            return None
        productoEntity.name = nombre
        productoEntity.description = descripcion
        productoEntity.price = precio
        productoEntity.category = categoria
        productoEntity.type = tipo
        productoEntity.diets = dietas.split(',') if dietas else []
        productoEntity.flavors = preferencia_sabor.split(',') if preferencia_sabor else []
        productoEntity.image_url = imagen_url
        return self.repository.actualizar(productoEntity)
    
    def eliminar_producto(self, producto_id):
        return self.repository.eliminar(producto_id)