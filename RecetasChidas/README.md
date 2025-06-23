# 🍽️ RecetasChidas - Plataforma E-commerce Culinaria

![Django](https://img.shields.io/badge/Django-4.2.20-green.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**RecetasChidas** es una plataforma e-commerce especializada en productos culinarios que ofrece comida preparada, kits de cocina, bebidas artesanales y postres gourmet, con filtrado por preferencias dietéticas específicas.

## 📋 Tabla de Contenidos

- [🚀 Características](#-características)
- [🏗️ Arquitectura](#️-arquitectura)
- [⚡ Instalación Rápida](#-instalación-rápida)
- [🔧 Configuración](#-configuración)
- [📊 Modelos de Datos](#-modelos-de-datos)
- [🎯 Uso](#-uso)
- [🧪 Testing](#-testing)
- [📚 API Reference](#-api-reference)
- [🤝 Contribuir](#-contribuir)
- [👥 Autores](#-autores)

## 🚀 Características

### 🍕 **Productos Culinarios**
- **Comida Preparada**: Platillos listos para consumir
- **Kits de Cocina**: Ingredientes pre-porcionados con recetas
- **Bebidas**: Smoothies, jugos naturales y bebidas artesanales
- **Postres**: Dulces artesanales y postres gourmet

### 🥗 **Filtros Dietéticos**
- ✅ Vegana
- ✅ Vegetariana  
- ✅ Sin Gluten
- ✅ Sin Lactosa
- ✅ Keto

### 🎨 **Preferencias de Sabor**
- 🧂 Salado
- 🍯 Dulce
- 🌶️ Picante
- 🍋 Agridulce

### 👥 **Sistema de Usuarios**
- **Clientes**: Navegación y compra de productos
- **Administradores**: Gestión completa del inventario

## 🏗️ Arquitectura

El proyecto implementa una **Arquitectura por Capas** con separación clara de responsabilidades:

```
┌─────────────────────────────────────────┐
│          🖥️ PRESENTATION LAYER          │
│    (Views, Templates, URLs, Forms)     │
├─────────────────────────────────────────┤
│           🔧 SERVICE LAYER              │
│       (Business Logic & Rules)         │
├─────────────────────────────────────────┤
│         🗄️ PERSISTENCE LAYER            │
│     (Repositories & Data Models)       │
├─────────────────────────────────────────┤
│           🎯 DOMAIN LAYER               │
│        (Entities & Schemas)             │
└─────────────────────────────────────────┘
```

### 🎨 **Patrones de Diseño Implementados**

| Patrón | Propósito | Ubicación |
|--------|-----------|-----------|
| **Repository** | Abstracción de acceso a datos | `persistence/repositories.py` |
| **Service Layer** | Lógica de negocio | `services/*.py` |
| **DTO/Entity** | Transferencia entre capas | `domain/schemas.py` |
| **Dependency Injection** | Flexibilidad en testing | Services |
| **Decorator** | Autorización y middleware | Views |
| **Factory Method** | Creación de entidades | Entities |

## ⚡ Instalación Rápida

### 📋 **Prerrequisitos**
- Python 3.9+
- MySQL 8.0+
- Git

### 🛠️ **Instalación**

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/recetas-chidas.git
cd recetas-chidas

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# 5. Ejecutar migraciones
python manage.py migrate

# 6. Poblar la base de datos (opcional)
python manage.py poblar_bd

# 7. Crear superusuario (opcional)
python manage.py createsuperuser

# 8. Ejecutar servidor de desarrollo
python manage.py runserver
```

🎉 **¡Listo!** Visita http://127.0.0.1:8000

## 🔧 Configuración

### 📄 **Variables de Entorno (.env)**

```env
# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=recetas_chidas_db
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306

# Django Settings
SECRET_KEY=tu_secret_key_super_segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 🗄️ **Configuración de Base de Datos**

**MySQL:**
```sql
CREATE DATABASE recetas_chidas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'tu_usuario'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON recetas_chidas_db.* TO 'tu_usuario'@'localhost';
FLUSH PRIVILEGES;
```

## 📊 Modelos de Datos

### 🏷️ **Entidades Principales**

```python
# Categoria
- id: int
- nombre: str
- descripcion: str

# Usuario  
- id: int
- nombre: str
- correo_electronico: str
- contrasena: str
- tipo_usuario: ['cliente', 'administrador']

# Producto
- id: int
- nombre: str
- descripcion: str
- precio: decimal
- categoria: ForeignKey(Categoria)
- tipo: ['comida preparada', 'kit de cocina', 'bebida', 'postre']
- dietas: str (CSV)
- preferencia_sabor: str (CSV)
- image_url: str

# Inventario
- id: int
- producto: ForeignKey(Producto)
- cantidad: int
```

### 🔗 **Relaciones**
- `Producto` ➡️ `Categoria` (Many-to-One)
- `Inventario` ➡️ `Producto` (One-to-One)

## 🎯 Uso

### 🌐 **Rutas Principales**

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | Login | Página de autenticación |
| `/home/` | Página Principal | Catálogo de productos |
| `/producto/detalle/<id>` | Detalle | Información del producto |
| `/panel/productos/` | Admin Panel | Gestión de productos |
| `/panel/editar/<id>/` | Editar | Modificar producto |
| `/categoria/` | Categorías | Listado de categorías |

### 🛠️ **Comandos de Gestión**

```bash
# Poblar base de datos con datos de ejemplo
python manage.py poblar_bd

# Diagnóstico de conexión a BD
python manage.py db_diagnostics

# Ver diagnóstico web
curl http://localhost:8000/db-diagnostics/
```

### 👤 **Sistema de Autenticación**

```python
# Decoradores de autorización
@usuario_requerido
def vista_protegida(request):
    # Solo usuarios autenticados

@administrador_requerido  
def panel_admin(request):
    # Solo administradores
```

## 🧪 Testing

### 🔬 **Ejecutar Tests**

```bash
# Todos los tests
python manage.py test

# Tests específicos
python manage.py test tienda.tests.ModeloTestCase

# Con cobertura
coverage run --source='.' manage.py test
coverage report
```

### 📝 **Estructura de Tests**

```
tienda/tests.py
├── ModeloTestCase       # Tests de modelos
├── RepositorioTestCase  # Tests de repositorios  
├── ServicioTestCase     # Tests de servicios
└── VistaTestCase       # Tests de vistas
```

## 📚 API Reference

### 📦 **Repositorios**

```python
# CategoriaRepositorio
obtener_todas() -> List[CategoriaEntity]
obtener_por_id(id: int) -> Optional[CategoriaEntity]
crear_categoria(entity: CategoriaEntity) -> CategoriaEntity
actualizar_categoria(entity: CategoriaEntity) -> CategoriaEntity
eliminar_categoria(id: int) -> bool

# ProductoRepositorio  
obtener_todos() -> List[ProductoEntity]
obtener_producto_por_id(id: int) -> Optional[ProductoEntity]
crearProducto(entity: ProductoEntity) -> ProductoEntity
actualizar(entity: ProductoEntity) -> ProductoEntity
eliminar(id: int) -> bool
```

### 🔧 **Servicios**

```python
# ProductoService
obtener_productos() -> List[ProductoEntity]
obtener_producto_por_id(id: int) -> Optional[ProductoEntity]  
crear_producto(nombre, descripcion, precio, ...) -> ProductoEntity
actualizar_producto(id, nombre, descripcion, ...) -> ProductoEntity
eliminar_producto(id: int) -> bool
```

## 🚀 **Stack Tecnológico**

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Django** | 4.2.20 | Framework web principal |
| **MySQL** | 8.0+ | Base de datos relacional |
| **Python** | 3.9+ | Lenguaje de programación |
| **python-decouple** | 3.8 | Gestión de variables de entorno |
| **mysqlclient** | 2.1.1 | Driver de MySQL |

## 🗂️ **Estructura del Proyecto**

```
RecetasChidas/
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 manage.py
├── 📄 .env
├── 📁 RecetasChidas/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── 📁 tienda/                 # App principal
    ├── 📁 domain/             # Entidades del dominio
    │   └── schemas.py
    ├── 📁 persistence/        # Capa de datos
    │   ├── models.py
    │   └── repositories.py
    ├── 📁 services/           # Lógica de negocio
    │   ├── categoria_service.py
    │   ├── producto_service.py
    │   ├── inventario_service.py
    │   └── usuario_service.py
    ├── 📁 presentation/       # Interfaz de usuario
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    └── 📁 management/         # Comandos personalizados
        └── commands/
            ├── poblar_bd.py
            └── db_diagnostics.py
```

## 🔒 **Seguridad**

- ✅ Variables de entorno para credenciales
- ✅ Validación de entrada en formularios
- ✅ Protección CSRF habilitada
- ✅ Sistema de autenticación personalizado
- ✅ Control de acceso basado en roles

## 📈 **Rendimiento**

- ⚡ Consultas optimizadas con select_related
- ⚡ Logging detallado para debugging
- ⚡ Configuración de conexión a BD optimizada
- ⚡ Templates cacheados en producción

## 🤝 Contribuir

### 📝 **Proceso de Contribución**

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### 📋 **Guías de Estilo**

- Seguir PEP 8 para Python
- Usar type hints en funciones públicas
- Documentar métodos complejos
- Escribir tests para nuevas funcionalidades

## 📝 **Changelog**

### v1.0.0 (2025-06-23)
- ✨ Sistema completo de gestión de productos
- ✨ Autenticación personalizada con roles
- ✨ Panel de administración
- ✨ Filtros por dietas y categorías
- ✨ Comandos de gestión personalizados

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 **Autores**

Este proyecto fue desarrollado por un equipo de estudiantes apasionados por la tecnología y la gastronomía:

| Autor | Rol | Contribución Principal |
|-------|-----|----------------------|
| **José de Jesús Almanza Contreras** | Lead Developer | Arquitectura del proyecto y Backend |
| **Pablo Emilio Alonso Romero** | Backend Developer | Analista y Backend |
| **Leonardo Gael Duran Torres** | Backend developer | Backend y base de datos |
| **Victor Hassiel Avila Monjaras** | Frontend Developer | Diseño de la interfaz grafica |
| **Jossue Amador Ynfante** | QA Engineer | Testing y control de calidad |

### 🤝 **Contacto del Equipo**
- **Organización**: Equipo RecetasChidas
- **Proyecto**: Plataforma E-commerce Culinaria
- **Año**: 2025

## 🙏 **Agradecimientos**

- Django Community por el excelente framework
- Unsplash por las imágenes de productos
- Contribuidores del proyecto

---

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐
