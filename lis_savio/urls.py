from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_treinos, name='lista_treinos'),
    path('adicionar/', views.adicionar_treino, name='adicionar_treino'),
    path('editar/<int:pk>/', views.editar_treino, name='editar_treino'),
    path('excluir/<int:pk>/', views.excluir_treino, name='excluir_treino'),
]
