from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='produtos'),
    path('meusprodutos/', views.meusprodutos, name='meusprodutos'),
    path('registrar/', views.registrar_produtos, name='registrar_produtos'),
    path('<id>/editar', views.editar_produto, name='editar_produto'),
    path('<id>/deletar', views.deletar_produto, name='deletar_produto'),
]