from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse, HttpResponseForbidden
import logging

from tienda.services.usuario_service import UsuarioService
from tienda.services.categoria_service import CategoriaService
from tienda.services.producto_service import ProductoService
from tienda.services.inventario_sevice import InventarioService
from functools import wraps
from django.shortcuts import redirect

usuario_service = UsuarioService()
categoria_service = CategoriaService()
producto_service = ProductoService()
inventario_service = InventarioService()

logger = logging.getLogger('tienda')

# Decorador para requerir que el usuario esté autenticado
def usuario_requerido(view_func):  # view_func es la función de vista original que se va a decorar
    @wraps(view_func)  # @wraps preserva el nombre y docstring de la función original decorada
    def _wrapped_view(request, *args, **kwargs):  # Esta función reemplazará a la vista original
        # Verifica si existe 'usuario_id' en la sesión (usuario autenticado)
        if not request.session.get('usuario_id'):
            # Si no está autenticado, redirige al login
            return redirect('login_view')
        # Si está autenticado, ejecuta la vista original con los mismos argumentos
        return view_func(request, *args, **kwargs)
    # Devuelve la función decorada
    return _wrapped_view

# Decorador para requerir que el usuario sea administrador
def administrador_requerido(view_func):  # view_func es la función de vista original que se va a decorar
    @wraps(view_func)  # @wraps preserva el nombre y docstring de la función original decorada
    def _wrapped_view(request, *args, **kwargs):  # Esta función reemplazará a la vista original
        # Verifica si el tipo de usuario en sesión es 'administrador'
        if request.session.get('usuario_tipo') != 'administrador':
            # Si no es administrador, redirige a la página principal
            return redirect('pagina_principal')
        # Si es administrador, ejecuta la vista original con los mismos argumentos
        return view_func(request, *args, **kwargs)
    # Devuelve la función decorada
    return _wrapped_view

def login_view(request):
    logger.info("🔐 Acceso a página de login")
    if request.session.get('usuario_id'):
        return redirect('pagina_principal')
    
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        
        logger.info(f"🔐 Intento de login para usuario: {email}")
        logger.info(f"🔐 Password recibido: {'*' * len(password) if password else 'vacío'}")

        usuario = usuario_service.buscar_usuario(email, password)
        
        if usuario:
            logger.info(f"✅ Autenticación exitosa para usuario: {email}")
            request.session['usuario_id'] = usuario['id']
            request.session['usuario_nombre'] = usuario['nombre']
            request.session['usuario_tipo'] = usuario['tipo_usuario']
            return redirect('pagina_principal')
        else:
            error_msg = f"❌ Credenciales inválidas para usuario: {email}"
            logger.warning(error_msg)
            messages.error(request, 'Credenciales inválidas. Por favor verifica tu usuario y contraseña.')

    return render(request, 'tienda/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login_view')

@usuario_requerido
def pagina_principal(request):
    logger.info(f"🏠 Acceso a página principal por usuario: {request.user.username if request.user.is_authenticated else 'Anónimo'}")
    
    try:
        filtro = request.GET.get('filtro', '')
        categorias = categoria_service.obtener_categorias()
        productos = producto_service.obtener_productos()
        
        logger.info(f"📊 Datos cargados - Categorías: {len(categorias)}, Productos: {len(productos)}")

        if filtro:
            productos = [p for p in productos if filtro.lower() in [d.lower() for d in getattr(p, 'diets', [])] or filtro.lower() == getattr(p, 'category', {}).get('name', '').lower()]
        
        # Log de consultas a la BD
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM tienda_categoria")
            cat_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM tienda_producto")
            prod_count = cursor.fetchone()[0]
            logger.info(f"🗃️ BD - Categorías en tabla: {cat_count}, Productos en tabla: {prod_count}")
        
        usuario = {
            'id': request.session.get('usuario_id'),
            'nombre': request.session.get('usuario_nombre'),
            'tipo': request.session.get('usuario_tipo')
        }

        return render(request, 'tienda/pagina_principal.html', {
            'categorias': categorias,
            'productos': productos,
            'usuario': usuario,
            'filtro': filtro
        })
    except Exception as e:
        logger.error(f"❌ Error cargando página principal: {e}")
        return render(request, 'tienda/pagina_principal.html', {
            'categorias': [],
            'productos': []
        })

@usuario_requerido
def detail_product_view(request, id):
    producto = producto_service.obtener_producto_por_id(id)
    usuario = {
            'id': request.session.get('usuario_id'),
            'nombre': request.session.get('usuario_nombre'),
            'tipo': request.session.get('usuario_tipo')
        }
    return render(request, 'tienda/detail_product.html', {'producto': producto, 'usuario': usuario})

@usuario_requerido
@administrador_requerido
def product_admin_view(request):
    productos = producto_service.obtener_productos()
    inventarios = inventario_service.obtener_inventarios()
    usuario = {
        'id': request.session.get('usuario_id'),
        'nombre': request.session.get('usuario_nombre'),
        'tipo': request.session.get('usuario_tipo')
    }
    return render(request, 'tienda/product_admin.html', {'productos': productos, 'inventarios': inventarios, 'usuario': usuario})

@usuario_requerido
@administrador_requerido
def category_view(request):
    categorias = categoria_service.obtener_categorias()
    usuario = {
        'id': request.session.get('usuario_id'),
        'nombre': request.session.get('usuario_nombre'),
        'tipo': request.session.get('usuario_tipo')
    }
    return render(request, 'tienda/categoria_admin.html', {'categorias': categorias, 'usuario': usuario})

@usuario_requerido
@administrador_requerido
def edit_category_view(request, id):
    categoria = categoria_service.obtener_categoria_por_id(id)
    usuario = {
        'id': request.session.get('usuario_id'),
        'nombre': request.session.get('usuario_nombre'),
        'tipo': request.session.get('usuario_tipo')
    }
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        try :
            categoria_service.actualizar_categoria(
                categoria_id=categoria.id,
                nombre=nombre,
                descripcion=descripcion
            )
        except ValueError as e:
            return HttpResponseForbidden(e)
        return redirect('category_admin')
    return render(request, 'tienda/edit_category.html', {'categoria': categoria, 'usuario': usuario})

@usuario_requerido
@administrador_requerido
def crear_categoria_view(request):
    usuario = {
        'id': request.session.get('usuario_id'),
        'nombre': request.session.get('usuario_nombre'),
        'tipo': request.session.get('usuario_tipo')
    }
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        try:
            categoria_service.crear_categoria(
                nombre=nombre,
                descripcion=descripcion
            )
            return redirect('category_admin')
        except ValueError as e:
            return HttpResponseForbidden(e)

    return render(request, 'tienda/edit_category.html', {'usuario': usuario})

@usuario_requerido
@administrador_requerido
def crear_producto_view(request):
    categorias = categoria_service.obtener_categorias()
    usuario = {
        'id': request.session.get('usuario_id'),
        'nombre': request.session.get('usuario_nombre'),
        'tipo': request.session.get('usuario_tipo')
    }

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio_str = request.POST.get('precio','')
        categoria_nombre = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        dietas = request.POST.getlist('dieta')
        preferencia = request.POST.get('preferencia')
        imagen_url = request.POST.get('imagen')
        inventario = request.POST.get('inventario')

        categoria = next((c for c in categorias if c.name == categoria_nombre), None)

        logger.info(f"POST DATA CREAR PRODUCTO: {dict(request.POST)}")
        try :
            if not precio_str:
                raise ValueError("El precio no puede estar vacío")
            else :
                precio = float(precio_str)

            if not inventario:
                if not dietas:
                    raise ValueError("Debe seleccionar al menos una dieta")
                if not categoria:
                    raise ValueError("Debe seleccionar una categoría")
                
            producto_creado = producto_service.crear_producto(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                categoria=categoria,
                tipo=tipo,
                dietas=','.join(dietas),
                preferencia_sabor=preferencia,
                imagen_url=imagen_url
            )

            if inventario:
                inventario_service.registrar_inventario(
                    productoId=producto_creado.id,
                    cantidad=inventario
                )
        except ValueError as e:
            return HttpResponseForbidden(e)

        logger.info(f"PRODUCTO CREADO: {(producto_creado)}")

        return redirect('product_admin')

    return render(request, 'tienda/edit_product.html', {'usuario': usuario, 'categorias': categorias})

@usuario_requerido
@administrador_requerido
def edit_product_view(request, id):
    producto = producto_service.obtener_producto_por_id(id)
    usuario = {
        'id': request.session.get('usuario_id'),
        'nombre': request.session.get('usuario_nombre'),
        'tipo': request.session.get('usuario_tipo')
    }
    categorias = categoria_service.obtener_categorias()
    inventario = inventario_service.obtener_inventario_por_producto(producto.id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio_str = request.POST.get('precio','')
        categoria_nombre = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        dietas = request.POST.getlist('dieta')
        preferencia = request.POST.get('preferencia')
        imagen_url = request.POST.get('imagen')
        cantidad = request.POST.get('inventario')

        categoria = next((c for c in categorias if c.name == categoria_nombre), None)

        try:
            if not precio_str:
                raise ValueError("El precio no puede estar vacío")
            else :
                precio = float(precio_str)

            producto_service.actualizar_producto(
                producto_id=producto.id,
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                categoria=categoria,
                tipo=tipo,
                dietas=','.join(dietas),
                preferencia_sabor=preferencia,
                imagen_url=imagen_url
            )

            if not inventario:
                if not dietas:
                    raise ValueError("Debe seleccionar al menos una dieta")
                if not categoria:
                    raise ValueError("Debe seleccionar una categoría")

            if inventario and cantidad is not None:
                inventario_service.actualizar_inventario(producto_id=producto.id, cantidad=cantidad)
        except ValueError as e:
            return HttpResponseForbidden(e)

        

        return redirect('product_admin')

    return render(request, 'tienda/edit_product.html', {'producto': producto, 'usuario': usuario, 'categorias': categorias, 'inventario': inventario})

@usuario_requerido
@administrador_requerido
def delete_category_view(request, id):
    categoria_service.eliminar_categoria_por_id(id)
    return redirect('category_admin')

@usuario_requerido
@administrador_requerido
def delete_product_view(request, id):
    producto_service.eliminar_producto(id)
    return redirect('product_admin')

# Vista de diagnóstico de base de datos
def db_diagnostics(request):
    """Vista para verificar la conexión a la base de datos y mostrar información"""
    try:
        # Obtener información de la conexión
        with connection.cursor() as cursor:
            # Verificar conexión
            cursor.execute("SELECT VERSION()")
            mysql_version = cursor.fetchone()[0]
            logger.info(f"✅ Conectado a MySQL versión: {mysql_version}")
            
            # Obtener información de la base de datos actual
            cursor.execute("SELECT DATABASE()")
            current_db = cursor.fetchone()[0]
            logger.info(f"✅ Base de datos actual: {current_db}")
            
            # Listar todas las tablas
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            logger.info(f"✅ Tablas encontradas: {tables}")
            
            # Verificar tablas específicas de Django
            django_tables = [table for table in tables if 'django' in table.lower()]
            auth_tables = [table for table in tables if 'auth' in table.lower()]
            tienda_tables = [table for table in tables if 'tienda' in table.lower()]
            
            logger.info(f"✅ Tablas de Django: {django_tables}")
            logger.info(f"✅ Tablas de autenticación: {auth_tables}")
            logger.info(f"✅ Tablas de tienda: {tienda_tables}")
            
            # Contar registros en algunas tablas importantes
            table_counts = {}
            for table in ['auth_user', 'tienda_categoria', 'tienda_producto']:
                if table in tables:
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    count = cursor.fetchone()[0]
                    table_counts[table] = count
                    logger.info(f"✅ Registros en {table}: {count}")
            
            diagnostics_data = {
                'mysql_version': mysql_version,
                'current_database': current_db,
                'all_tables': tables,
                'django_tables': django_tables,
                'auth_tables': auth_tables,
                'tienda_tables': tienda_tables,
                'table_counts': table_counts,
                'status': 'success'
            }
            
            return JsonResponse(diagnostics_data, json_dumps_params={'indent': 2})
            
    except Exception as e:
        error_msg = f"❌ Error de conexión a la base de datos: {str(e)}"
        logger.error(error_msg)
        return JsonResponse({
            'status': 'error',
            'error': error_msg
        })
