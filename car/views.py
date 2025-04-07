from django.shortcuts import render, redirect
from .forms import CarroForm
from .models import Carro

def home(request):
    contexto = {'titulo': 'Página Inicial'}
    return render(request, 'car/index.html', contexto)


def adicionar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carros')  # Redireciona para uma página de sucesso ou lista
    else:
        form = CarroForm()

    return render(request, 'car/adicionar_carro.html', {'form': form})


def lista_carros(request):
    carros = Carro.objects.all().order_by('-data_cadastro')
    return render(request, 'car/lista_carros.html', {'carros': carros})