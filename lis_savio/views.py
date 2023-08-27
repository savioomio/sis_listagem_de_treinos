# Importa as funções necessárias do módulo 'django.shortcuts'
from django.shortcuts import render, get_object_or_404, redirect
# Importa o modelo 'Treino' e o formulário 'TreinoForm' do diretório atual
from .models import Treino
from .forms import TreinoForm

# Função para listar os treinos e agrupá-los por categoria
def lista_treinos(request):
    # Obtém todos os objetos 'Treino' do banco de dados
    treinos = Treino.objects.all()
    categorias = {}  # Dicionário para agrupar treinos por categoria
    for treino in treinos:
        if treino.categoria in categorias:
            categorias[treino.categoria].append(treino)
        else:
            categorias[treino.categoria] = [treino]
    # Renderiza o template 'lista_treinos.html', passando o dicionário de categorias como contexto
    return render(request, 'lis_savio/lista_treinos.html', {'categorias': categorias})

# Função para adicionar um novo treino
def adicionar_treino(request):
    if request.method == 'POST':
        # Cria um formulário 'TreinoForm' com os dados do POST e arquivos enviados
        form = TreinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salva o objeto 'Treino' no banco de dados
            return redirect('lista_treinos')  # Redireciona para a lista de treinos
    else:
        form = TreinoForm()  # Cria um novo formulário vazio
    # Renderiza o template 'adicionar_treino.html', passando o formulário como contexto
    return render(request, 'lis_savio/adicionar_treino.html', {'form': form})

# Função para editar um treino existente
def editar_treino(request, pk):
    treino = get_object_or_404(Treino, pk=pk)  # Obtém o objeto 'Treino' pelo ID (pk)
    if request.method == 'POST':
        # Cria um formulário 'TreinoForm' preenchido com os dados do POST e arquivos enviados
        form = TreinoForm(request.POST, request.FILES, instance=treino)
        if form.is_valid():
            form.save()  # Salva as alterações no objeto 'Treino'
            return redirect('lista_treinos')  # Redireciona para a lista de treinos
    else:
        form = TreinoForm(instance=treino)  # Cria um formulário preenchido com os dados do treino
    # Renderiza o template 'editar_treino.html', passando o formulário como contexto
    return render(request, 'lis_savio/editar_treino.html', {'form': form})

# Função para excluir um treino existente
def excluir_treino(request, pk):
    treino = get_object_or_404(Treino, pk=pk)  # Obtém o objeto 'Treino' pelo ID (pk)
    if request.method == 'POST':
        treino.delete()  # Remove o objeto 'Treino' do banco de dados
        return redirect('lista_treinos')  # Redireciona para a lista de treinos
    # Renderiza o template 'excluir_treino.html', passando o treino como contexto
    return render(request, 'lis_savio/excluir_treino.html', {'treino': treino})
