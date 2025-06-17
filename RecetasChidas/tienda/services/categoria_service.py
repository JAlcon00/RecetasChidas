from tienda.persistence.repositories import CategoriaRepositorio

class CategoriaService:
    @staticmethod
    def registrar_categoria(nombre, descripcion=''):
        return CategoriaRepositorio.crear(
            nombre=nombre,
            descripcion=descripcion
        )

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
