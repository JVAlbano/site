from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_user'),
    path('cadastro/', views.cadastro, name='cadastro_user'),
    path('logout', views.logout, name='logout'),
    path('<username>editar_usuario/', views.editar_usuario, name='editar_usuario'),
]