from django.core.management.base import BaseCommand
from tienda.persistence.models import Categoria, Producto
from django.db import transaction


class Command(BaseCommand):
    help = 'Poblará la base de datos con categorías y productos de ejemplo'

    def handle(self, *args, **options):
        self.stdout.write(self.style.HTTP_INFO('🍽️ POBLANDO BASE DE DATOS CON DATOS DE EJEMPLO'))
        self.stdout.write('=' * 60)
        
        try:
            with transaction.atomic():
                # Crear categorías
                categorias_data = [
                    {
                        'nombre': 'Comida Preparada',
                        'descripcion': 'Platillos listos para comer, frescos y deliciosos'
                    },
                    {
                        'nombre': 'Kit de Cocina',
                        'descripcion': 'Ingredientes pre-portionados con recetas para cocinar en casa'
                    },
                    {
                        'nombre': 'Bebidas',
                        'descripcion': 'Bebidas naturales, jugos y smoothies'
                    },
                    {
                        'nombre': 'Postres',
                        'descripcion': 'Dulces artesanales y postres gourmet'
                    }
                ]
                
                categorias_creadas = []
                for cat_data in categorias_data:
                    categoria, created = Categoria.objects.get_or_create(
                        nombre=cat_data['nombre'],
                        defaults={'descripcion': cat_data['descripcion']}
                    )
                    categorias_creadas.append(categoria)
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'✅ Categoría creada: {categoria.nombre}')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'⚠️  Categoría ya existe: {categoria.nombre}')
                        )
                
                # Crear productos
                productos_data = [
                    # Comida Preparada
                    {
                        'nombre': 'Ensalada Vegana Mediterránea',
                        'descripcion': 'Mezcla fresca de vegetales con aderezo de tahini',
                        'precio': 12.50,
                        'categoria': 'Comida Preparada',
                        'tipo': 'comida preparada',
                        'dietas': 'vegana,vegetariana,sin_gluten',
                        'preferencia_sabor': 'salado',
                        'image_url': 'https://images.unsplash.com/photo-1606787366850-de6330128bfc?auto=format&fit=crop&w=400&q=80'
                    },
                    {
                        'nombre': 'Pollo Teriyaki con Arroz',
                        'descripcion': 'Pollo glaseado en salsa teriyaki con arroz integral y brócoli',
                        'precio': 18.75,
                        'categoria': 'Comida Preparada',
                        'tipo': 'comida preparada',
                        'dietas': 'sin_gluten',
                        'preferencia_sabor': 'salado',
                        'image_url': 'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=400&q=80'
                    },
                    {
                        'nombre': 'Tacos de Carnitas Picantes',
                        'descripcion': 'Tres tacos con carnitas de cerdo, salsa verde y cebolla morada',
                        'precio': 15.25,
                        'categoria': 'Comida Preparada',
                        'tipo': 'comida preparada',
                        'dietas': '',
                        'preferencia_sabor': 'picante',
                        'image_url': 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?auto=format&fit=crop&w=400&q=80'
                    },
                    
                    # Kit de Cocina
                    {
                        'nombre': 'Kit Mexicano - Chiles en Nogada',
                        'descripcion': 'Ingredientes para preparar chiles poblanos rellenos con nogada',
                        'precio': 25.00,
                        'categoria': 'Kit de Cocina',
                        'tipo': 'kit de cocina',
                        'dietas': 'vegetariana',
                        'preferencia_sabor': 'salado',
                        'image_url': 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?auto=format&fit=crop&w=400&q=80'
                    },
                    {
                        'nombre': 'Kit Italiano - Pasta Carbonara',
                        'descripcion': 'Kit completo para preparar pasta carbonara auténtica italiana',
                        'precio': 22.50,
                        'categoria': 'Kit de Cocina',
                        'tipo': 'kit de cocina',
                        'dietas': '',
                        'preferencia_sabor': 'salado',
                        'image_url': 'https://images.unsplash.com/photo-1506368083636-6defb67639d1?auto=format&fit=crop&w=400&q=80'
                    },
                    {
                        'nombre': 'Kit Vegano - Curry de Lentejas',
                        'descripcion': 'Ingredientes para curry de lentejas rojas con leche de coco',
                        'precio': 19.75,
                        'categoria': 'Kit de Cocina',
                        'tipo': 'kit de cocina',
                        'dietas': 'vegana,vegetariana,sin_gluten',
                        'preferencia_sabor': 'picante',
                        'image_url': 'https://images.unsplash.com/photo-1598514982461-6fe9c2e8c8ce?auto=format&fit=crop&w=400&q=80'
                    },
                    
                    # Bebidas
                    {
                        'nombre': 'Smoothie Verde Detox',
                        'descripcion': 'Espinaca, piña, mango y jengibre',
                        'precio': 8.50,
                        'categoria': 'Bebidas',
                        'tipo': 'bebida',
                        'dietas': 'vegana,vegetariana,sin_gluten',
                        'preferencia_sabor': 'dulce',
                        'image_url': 'https://images.unsplash.com/photo-1610970881699-44a5587cabec?auto=format&fit=crop&w=400&q=80'
                    },
                    {
                        'nombre': 'Agua de Jamaica con Chía',
                        'descripcion': 'Refrescante agua de jamaica con semillas de chía',
                        'precio': 6.75,
                        'categoria': 'Bebidas',
                        'tipo': 'bebida',
                        'dietas': 'vegana,vegetariana,sin_gluten',
                        'preferencia_sabor': 'dulce',
                        'image_url': 'https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=400&q=80'
                    },
                    
                    # Postres
                    {
                        'nombre': 'Cheesecake de Fresa Vegano',
                        'descripcion': 'Cheesecake a base de anacardos con coulis de fresa',
                        'precio': 14.25,
                        'categoria': 'Postres',
                        'tipo': 'postre',
                        'dietas': 'vegana,vegetariana',
                        'preferencia_sabor': 'dulce',
                        'image_url': 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=400&q=80'
                    },
                    {
                        'nombre': 'Brownie de Chocolate Sin Gluten',
                        'descripcion': 'Brownie húmedo hecho con harina de almendra',
                        'precio': 11.50,
                        'categoria': 'Postres',
                        'tipo': 'postre',
                        'dietas': 'sin_gluten,vegetariana',
                        'preferencia_sabor': 'dulce',
                        'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=400&q=80'
                    }
                ]
                
                productos_creados = 0
                for prod_data in productos_data:
                    # Buscar la categoría
                    try:
                        categoria = Categoria.objects.get(nombre=prod_data['categoria'])
                    except Categoria.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR(f'❌ Categoría no encontrada: {prod_data["categoria"]}')
                        )
                        continue
                    
                    producto, created = Producto.objects.get_or_create(
                        nombre=prod_data['nombre'],
                        defaults={
                            'descripcion': prod_data['descripcion'],
                            'precio': prod_data['precio'],
                            'categoria': categoria,
                            'tipo': prod_data['tipo'],
                            'dietas': prod_data['dietas'],
                            'preferencia_sabor': prod_data['preferencia_sabor'],
                            'image_url': prod_data['image_url']
                        }
                    )
                    
                    if created:
                        productos_creados += 1
                        self.stdout.write(
                            self.style.SUCCESS(f'✅ Producto creado: {producto.nombre} (${producto.precio})')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'⚠️  Producto ya existe: {producto.nombre}')
                        )
                
                # Resumen
                self.stdout.write('\n' + '=' * 60)
                self.stdout.write(
                    self.style.HTTP_INFO(f'📊 RESUMEN:')
                )
                self.stdout.write(f'   📂 Categorías totales: {Categoria.objects.count()}')
                self.stdout.write(f'   🛍️  Productos totales: {Producto.objects.count()}')
                self.stdout.write(f'   ✨ Productos creados en esta ejecución: {productos_creados}')
                
                self.stdout.write('\n' + self.style.SUCCESS('🎉 ¡Base de datos poblada exitosamente!'))
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error poblando la base de datos: {e}')
            )
