from tienda.persistence.repositories import CategoriaRepositorio

class CategoriaService:
    def __init__(self, repository=None):
        self.repository = repository or CategoriaRepositorio
        pass

    def obtener_categorias(self):
        categorias = self.repository.obtener_todas()
        return categorias

    @staticmethod
    def obtener_categorias():
        return CategoriaRepositorio.obtener_todas()

    @staticmethod
    def obtener_categoria_por_id(categoria_id):
        return CategoriaRepositorio.obtener_por_id(categoria_id)

    @staticmethod
    def actualizar_categoria(categoria, **kwargs):
        return CategoriaRepositorio.actualizar(categoria, **kwargs)

    @staticmethod
    def eliminar_categoria(categoria):
        CategoriaRepositorio.eliminar(categoria)
