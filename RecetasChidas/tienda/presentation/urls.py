from django.urls import path
from tienda.presentation.views import pagina_principal, login_view, db_diagnostics
from django.contrib.auth.views import LogoutView
from tienda.presentation import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.pagina_principal, name='pagina_principal'),
    path('producto/detalle/<int:id>', views.detail_product_view, name='detail_product'),
    path('panel/productos/', views.product_admin_view, name='product_admin'),
    path('panel/categorias/', views.category_view, name='category_admin'),
    path('panel/categoria/crear/', views.crear_categoria_view, name='crear_categoria'),
    path('panel/producto/crear/', views.crear_producto_view, name='crear_producto'),
    path('panel/editar/<int:id>/', views.edit_product_view, name='edit_product'),
    path('panel/editar/categoria/<int:id>/', views.edit_category_view, name='edit_category'),
    path('panel/delete/producto/<int:id>/', views.delete_product_view, name='delete_product'),
    path('panel/delete/categoria/<int:id>/', views.delete_category_view, name='delete_category'),
    path('db-diagnostics/', views.db_diagnostics, name='db_diagnostics'),
    
    # ...otras rutas...
]
