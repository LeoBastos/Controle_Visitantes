from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard.views import index
from visitantes.views import registrar_visitante, buscar_visitante, finalizar_visita

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registrar-visitante/', registrar_visitante, name='registrar_visitante'),
    path('visitantes/<int:id>/', buscar_visitante, name='buscar_visitante'),
    path('visitantes/<int:id>/finalizar', finalizar_visita, name='finalizar_visita'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
