from tienda.persistence.repositories.categoria_repositorie import CategoriaRepositorio
from tienda.domain.schemas import CategoriaEntity

class CategoriaService:
    def __init__(self, repository=None):
        self.repository = repository or CategoriaRepositorio
        pass

    def validar_categoria(self, categoria:str, descripcion:str):
        if not categoria:
            raise ValueError("El nombre de la categoria no puede estar vacio")
        if not descripcion:
            raise ValueError("La descripcion de la categoria no puede estar vacia")

    def obtener_categorias(self):
        categorias = self.repository.obtener_todas()
        return categorias
    
    def obtener_categoria_por_id(self, categoria_id):
        # Obtener una categoria por su id
        categoria = self.repository.obtener_por_id(categoria_id)
        return categoria
    
    def obtener_categoria_por_nombre(self, nombre:str):
        categoria = self.repository.obtener_por_nombre(nombre)
        return categoria

    def crear_categoria(self, nombre:str, descripcion:str):
        # Crear una categoria nueva
        self.validar_categoria(nombre, descripcion)
        categoriaEntity = CategoriaEntity.create(name=nombre, description=descripcion)
        return self.repository.crear_categoria(categoriaEntity)

    def actualizar_categoria(self, categoria_id:int, nombre:str, descripcion:str):
        self.validar_categoria(nombre, descripcion)

        # Actualizar una categoria existente
        categoriaEntity = self.repository.obtener_por_id(categoria_id)
        if not categoriaEntity:
            return None
        categoriaEntity.name = nombre
        categoriaEntity.description = descripcion
        return self.repository.actualizar_categoria(categoriaEntity)
        
    def eliminar_categoria_por_id(self, categoria_id:int):
        # Eliminar una categoria por su id
        return self.repository.eliminar_categoria(categoria_id)
