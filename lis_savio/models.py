# Importa a classe 'models' do módulo 'django.db'
from django.db import models

# Define a classe 'Treino' que herda de 'models.Model'
class Treino(models.Model):
    # Define um campo de caracteres para o nome, com no máximo 100 caracteres
    nome = models.CharField(max_length=100)
    
    # Define um campo de caracteres para a categoria, com um conjunto limitado de escolhas
    categoria = models.CharField(max_length=9, choices=[
        ('Treino(A)', 'Treino-A'),
        ('Treino(B)', 'Treino-B'),
        ('Treino(C)', 'Treino-C'),
        ('Treino(D)', 'Treino-D'),
        ('Treino(E)', 'Treino-E'),
    ])
    
    # Define um campo de imagem para a imagem, com local de upload personalizado
    imagem = models.ImageField(upload_to='img_treinos/', blank=True, null=True)
    
    # Define o método __str__ que retorna a representação em string do objeto
    def __str__(self):
        return self.nome
