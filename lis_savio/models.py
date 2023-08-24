from django.db import models

from django.db import models

class Treino(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=9, choices=[
        ('Treino(A)', 'Treino-A'),
        ('Treino(B)', 'Treino-B'),
        ('Treino(C)', 'Treino-C'),
        ('Treino(D)', 'Treino-D'),
        ('Treino(E)', 'Treino-E'),
    ])
    imagem = models.ImageField(upload_to='img_treinos/', blank=True, null=True)

    def __str__(self):
        return self.nome
