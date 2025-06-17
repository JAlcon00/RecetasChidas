from django.urls import path
from tienda.presentation.views import pagina_principal, login_view, db_diagnostics
from django.contrib.auth.views import LogoutView
from tienda.presentation import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.pagina_principal, name='pagina_principal'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('db-diagnostics/', views.db_diagnostics, name='db_diagnostics'),
    # ...otras rutas...
]
