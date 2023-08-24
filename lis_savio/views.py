from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Treino
from .forms import TreinoForm  

def lista_treinos(request):
    treinos = Treino.objects.all()
    categorias = {}  # Dicionário para agrupar treinos por categoria
    for treino in treinos:
        if treino.categoria in categorias:
            categorias[treino.categoria].append(treino)
        else:
            categorias[treino.categoria] = [treino]
    return render(request, 'lis_savio/lista_treinos.html', {'categorias': categorias})


def adicionar_treino(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('lista_treinos')
    else:
        form = TreinoForm()
    return render(request, 'lis_savio/adicionar_treino.html', {'form': form})

def editar_treino(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    if request.method == 'POST':
        form = TreinoForm(request.POST, request.FILES, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('lista_treinos')
    else:
        form = TreinoForm(instance=treino)
    return render(request, 'lis_savio/editar_treino.html', {'form': form})


def excluir_treino(request, pk):
    treino = get_object_or_404(Treino, pk=pk)
    if request.method == 'POST':
        treino.delete()
        return redirect('lista_treinos')
    return render(request, 'lis_savio/excluir_treino.html', {'treino': treino})
