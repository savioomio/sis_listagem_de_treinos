from django.urls import path
# Importa as views definidas no mesmo diretório
from . import views

# Lista de URLs do aplicativo
urlpatterns = [
    # Mapeia a URL raiz para a função 'lista_treinos' na view, nomeando-a como 'lista_treinos'
    path('', views.lista_treinos, name='lista_treinos'),
    # Mapeia a URL 'adicionar/' para a função 'adicionar_treino' na view, nomeando-a como 'adicionar_treino'
    path('adicionar/', views.adicionar_treino, name='adicionar_treino'),
    # Mapeia a URL 'editar/<int:pk>/' para a função 'editar_treino' na view, nomeando-a como 'editar_treino'
    path('editar/<int:pk>/', views.editar_treino, name='editar_treino'),
    # Mapeia a URL 'excluir/<int:pk>/' para a função 'excluir_treino' na view, nomeando-a como 'excluir_treino'
    path('excluir/<int:pk>/', views.excluir_treino, name='excluir_treino'),
]
