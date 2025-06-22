from tienda.persistence.repositories import CategoriaRepositorio
from tienda.domain.schemas import CategoriaEntity

class CategoriaService:
    def __init__(self, repository=None):
        self.repository = repository or CategoriaRepositorio
        pass

    def obtener_categorias(self):
        categorias = self.repository.obtener_todas()
        return categorias
    
    def obtener_categoria_por_id(self, categoria_id):
        # Obtener una categoria por su id
        categoria = self.repository.obtener_por_id(categoria_id)
        return categoria

    def crear_categoria(self, nombre:str, descripcion:str):
        # Crear una categoria nueva
        categoriaEntity = CategoriaEntity.create(nombre=nombre, description=descripcion)
        return self.repository.crear_categoria(categoriaEntity)

    def actualizar_categoria(self, categoria_id:int, nombre:str, descripcion:str):
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
