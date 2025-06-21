from django.urls import path
from tienda.presentation.views import pagina_principal, login_view, db_diagnostics
from django.contrib.auth.views import LogoutView
from tienda.presentation import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.pagina_principal, name='pagina_principal'),
    path('producto/detalle/<int:id>', views.detail_product_view, name='detail_product'),
    path('db-diagnostics/', views.db_diagnostics, name='db_diagnostics'),
    path('panel/principal/', views.principal_admin_view, name='principal_admin'),
    path('panel/productos/', views.product_admin_view, name='product_admin'),
    path('panel/producto/<int:id>/', views.product_detail_admin_view, name='product_detail_admin'),
    path('categoria/', views.category_view, name='category'),
    path('producto/editar/', views.edit_product_view, name='edit_product'),
    
    # ...otras rutas...
]
