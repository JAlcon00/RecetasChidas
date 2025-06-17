from django.core.management.base import BaseCommand
from django.db import connection
from django.contrib.auth.models import User
from tienda.persistence.models import Categoria, Producto


class Command(BaseCommand):
    help = 'Diagnostica la conexión a la base de datos MySQL y muestra información detallada'

    def handle(self, *args, **options):
        self.stdout.write(self.style.HTTP_INFO('🔍 DIAGNÓSTICO DE BASE DE DATOS MySQL'))
        self.stdout.write('=' * 60)
        
        try:
            # Información de conexión
            with connection.cursor() as cursor:
                # Versión de MySQL
                cursor.execute("SELECT VERSION()")
                mysql_version = cursor.fetchone()[0]
                self.stdout.write(
                    self.style.SUCCESS(f'✅ MySQL Version: {mysql_version}')
                )
                
                # Base de datos actual
                cursor.execute("SELECT DATABASE()")
                current_db = cursor.fetchone()[0]
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Base de datos: {current_db}')
                )
                
                # Host info
                cursor.execute("SELECT @@hostname")
                hostname = cursor.fetchone()[0]
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Host: {hostname}')
                )
                
                # Usuario actual
                cursor.execute("SELECT USER()")
                current_user = cursor.fetchone()[0]
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Usuario conectado: {current_user}')
                )
                
                # Listar todas las tablas
                cursor.execute("SHOW TABLES")
                tables = [table[0] for table in cursor.fetchall()]
                self.stdout.write(
                    self.style.HTTP_INFO(f'📋 Total de tablas: {len(tables)}')
                )
                
                # Tablas específicas de Django
                django_tables = [t for t in tables if 'django' in t.lower()]
                auth_tables = [t for t in tables if 'auth' in t.lower()]
                tienda_tables = [t for t in tables if 'tienda' in t.lower()]
                
                self.stdout.write('\n📊 TABLAS POR CATEGORÍA:')
                self.stdout.write(f'   Django: {len(django_tables)} tablas')
                self.stdout.write(f'   Auth: {len(auth_tables)} tablas')
                self.stdout.write(f'   Tienda: {len(tienda_tables)} tablas')
                
                # Mostrar todas las tablas
                self.stdout.write('\n📋 TODAS LAS TABLAS:')
                for i, table in enumerate(tables, 1):
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    count = cursor.fetchone()[0]
                    self.stdout.write(f'   {i:2d}. {table:<30} ({count:>6} registros)')
                
                # Verificar modelos específicos
                self.stdout.write('\n🔍 VERIFICACIÓN DE MODELOS:')
                
                # Usuarios
                user_count = User.objects.count()
                self.stdout.write(f'   👥 Usuarios: {user_count}')
                
                # Categorías
                try:
                    cat_count = Categoria.objects.count()
                    self.stdout.write(f'   📂 Categorías: {cat_count}')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'   ❌ Error en Categorías: {e}')
                    )
                
                # Productos
                try:
                    prod_count = Producto.objects.count()
                    self.stdout.write(f'   🛍️  Productos: {prod_count}')
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'   ❌ Error en Productos: {e}')
                    )
                
                # Estado de migraciones
                self.stdout.write('\n📋 ESTADO DE MIGRACIONES:')
                cursor.execute("SELECT app, name FROM django_migrations ORDER BY app, name")
                migrations = cursor.fetchall()
                
                apps_migrations = {}
                for app, name in migrations:
                    if app not in apps_migrations:
                        apps_migrations[app] = 0
                    apps_migrations[app] += 1
                
                for app, count in apps_migrations.items():
                    self.stdout.write(f'   {app}: {count} migraciones aplicadas')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error de conexión: {e}')
            )
            return
        
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(
            self.style.SUCCESS('✅ Diagnóstico completado exitosamente!')
        )
