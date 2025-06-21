from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
import logging

from tienda.services.categoria_service import CategoriaService
from tienda.services.producto_service import ProductoService
from tienda.services.inventario_sevice import InventarioService
from tienda.services.usuario_service import UsuarioService
from tienda.persistence.models import Categoria, Producto, Inventario, Usuario
from tienda.forms import CategoriaForm, ProductoForm, InventarioForm, UsuarioForm

logger = logging.getLogger('tienda')

def index(request):
    if request.user.is_authenticated:
        return redirect('pagina_principal')
    else:
        return redirect('login_view')

# Vistas de Categoría
@login_required
def lista_categorias(request):
    categorias = CategoriaService.obtener_categorias()
    return render(request, 'tienda/lista_categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            CategoriaService.registrar_categoria(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion']
            )
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'tienda/crear_categoria.html', {'form': form})

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            CategoriaService.actualizar_categoria(
                categoria,
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion']
            )
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'tienda/editar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        CategoriaService.eliminar_categoria(categoria)
        return redirect('lista_categorias')
    return render(request, 'tienda/eliminar_categoria.html', {'categoria': categoria})

# Vistas de Producto
@login_required
def lista_productos(request):
    productos = ProductoService.obtener_productos()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            ProductoService.registrar_producto(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                categoria=form.cleaned_data['categoria'],
                tipo=form.cleaned_data['tipo'],
                dietas=form.cleaned_data.get('dietas', ''),
                preferencia_sabor=form.cleaned_data.get('preferencia_sabor', ''),
                imagen_url=form.cleaned_data.get('imagen_url', 'https://example.com/default.jpg')
            )
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/crear_producto.html', {'form': form})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            ProductoService.actualizar_producto(
                producto,
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                categoria=form.cleaned_data['categoria'],
                tipo=form.cleaned_data['tipo'],
                dietas=form.cleaned_data.get('dietas', ''),
                preferencia_sabor=form.cleaned_data.get('preferencia_sabor', ''),
                imagen_url=form.cleaned_data.get('imagen_url', 'https://example.com/default.jpg')
            )
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        ProductoService.eliminar_producto(producto)
        return redirect('lista_productos')
    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})

# Vistas de Inventario
@login_required
def lista_inventario(request):
    inventarios = InventarioService.obtener_inventarios()
    return render(request, 'tienda/lista_inventario.html', {'inventarios': inventarios})

@login_required
def crear_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            InventarioService.registrar_inventario(
                producto=form.cleaned_data['producto'],
                cantidad=form.cleaned_data['cantidad']
            )
            return redirect('lista_inventario')
    else:
        form = InventarioForm()
    return render(request, 'tienda/crear_inventario.html', {'form': form})

@login_required
def editar_inventario(request, inventario_id):
    inventario = get_object_or_404(Inventario, id=inventario_id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            InventarioService.actualizar_inventario(
                inventario,
                producto=form.cleaned_data['producto'],
                cantidad=form.cleaned_data['cantidad']
            )
            return redirect('lista_inventario')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'tienda/editar_inventario.html', {'form': form, 'inventario': inventario})

@login_required
def eliminar_inventario(request, inventario_id):
    inventario = get_object_or_404(Inventario, id=inventario_id)
    if request.method == 'POST':
        InventarioService.eliminar_inventario(inventario)
        return redirect('lista_inventario')
    return render(request, 'tienda/eliminar_inventario.html', {'inventario': inventario})

# Vistas de Usuario (ejemplo básico)
@login_required
def lista_usuarios(request):
    usuarios = UsuarioService.obtener_usuarios()
    return render(request, 'tienda/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            UsuarioService.registrar_usuario(
                nombre=form.cleaned_data['nombre'],
                correo_electronico=form.cleaned_data['correo_electronico'],
                contrasena=form.cleaned_data['contrasena'],
                tipo_usuario=form.cleaned_data.get('tipo_usuario', 'cliente')
            )
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'tienda/crear_usuario.html', {'form': form})

@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            UsuarioService.actualizar_usuario(
                usuario,
                nombre=form.cleaned_data['nombre'],
                correo_electronico=form.cleaned_data['correo_electronico'],
                contrasena=form.cleaned_data['contrasena'],
                tipo_usuario=form.cleaned_data.get('tipo_usuario', 'cliente')
            )
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'tienda/editar_usuario.html', {'form': form, 'usuario': usuario})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        UsuarioService.eliminar_usuario(usuario)
        return redirect('lista_usuarios')
    return render(request, 'tienda/eliminar_usuario.html', {'usuario': usuario})

# Página principal

@login_required
def pagina_principal(request):
    logger.info(f"🏠 Acceso a página principal por usuario: {request.user.username if request.user.is_authenticated else 'Anónimo'}")
    
    try:
        categorias = CategoriaService.obtener_categorias()
        productos = ProductoService.obtener_productos()
        
        logger.info(f"📊 Datos cargados - Categorías: {len(categorias)}, Productos: {len(productos)}")
        
        # Log de consultas a la BD
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM tienda_categoria")
            cat_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM tienda_producto")
            prod_count = cursor.fetchone()[0]
            logger.info(f"🗃️ BD - Categorías en tabla: {cat_count}, Productos en tabla: {prod_count}")
        
        return render(request, 'tienda/usuario/pagina_principal.html', {
            'categorias': categorias,
            'productos': productos
        })
    except Exception as e:
        logger.error(f"❌ Error cargando página principal: {e}")
        return render(request, 'tienda/usuario/pagina_principal.html', {
            'categorias': [],
            'productos': []
        })

# Detalle de producto

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'tienda/detail_product.html', {'producto': producto})

# Vista de Login personalizada
def login_view(request):
    logger.info("🔐 Acceso a página de login")
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        logger.info(f"🔐 Intento de login para usuario: {username}")
        logger.info(f"🔐 Password recibido: {'*' * len(password) if password else 'vacío'}")
        
        # Verificar conexión a BD antes de autenticar
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM auth_user WHERE username = %s", [username])
                user_exists = cursor.fetchone()[0] > 0
                logger.info(f"🔍 Usuario '{username}' existe en BD: {user_exists}")
        except Exception as e:
            logger.error(f"❌ Error verificando usuario en BD: {e}")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            logger.info(f"✅ Autenticación exitosa para usuario: {username}")
            login(request, user)
            logger.info(f"✅ Login completado, redirigiendo a página principal")
            messages.success(request, f'¡Bienvenido {username}!')
            return redirect('pagina_principal')
        else:
            error_msg = f"❌ Credenciales inválidas para usuario: {username}"
            logger.warning(error_msg)
            messages.error(request, 'Credenciales inválidas. Por favor verifica tu usuario y contraseña.')
    
    return render(request, 'tienda/login.html')

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

@login_required
def principal_admin_view(request):
    return render(request, 'tienda/principal_admin.html')

@login_required
def product_admin_view(request):
    productos = ProductoService.obtener_productos()
    return render(request, 'tienda/product_admin.html', {'productos': productos})

@login_required
def product_detail_admin_view(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/product_detail_admin.html', {'producto': producto})

@login_required
def category_view(request):
    categorias = CategoriaService.obtener_categorias()
    return render(request, 'tienda/category.html', {'categorias': categorias})

@login_required
def detail_product_view(request):
    producto_id = request.GET.get('id')
    producto = get_object_or_404(Producto, id=producto_id) if producto_id else None
    return render(request, 'tienda/detail_product.html', {'producto': producto})

@login_required
def edit_product_view(request):
    producto_id = request.GET.get('id')
    producto = get_object_or_404(Producto, id=producto_id) if producto_id else None
    if request.method == 'POST' and producto:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('product_admin')
    else:
        form = ProductoForm(instance=producto) if producto else ProductoForm()
    return render(request, 'tienda/edit_product.html', {'form': form, 'producto': producto})
