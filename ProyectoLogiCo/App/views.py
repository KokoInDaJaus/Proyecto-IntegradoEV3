from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmacia, Moto, Motorista
from .forms import FarmaciaForm, MotoForm, MotoristaForm
from App import views


def index(request):
    return render(request, 'index.html')

def paginaPrincipal(request):
    return render(request, 'paginaPrincipal.html')

# ========== FARMACIA ==========
def farmacia_list(request):
    farmacias = Farmacia.objects.all()
    return render(request, 'farmacia_list.html', {'farmacias': farmacias})




def farmacia_create(request):
    if request.method == 'POST':
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmacia_list')
    else:
        form = FarmaciaForm()
    return render(request, 'farmacia_form.html', {'form': form})

def farmacia_update(request, pk):
    farmacia = get_object_or_404(Farmacia, pk=pk)
    if request.method == 'POST':
        form = FarmaciaForm(request.POST, instance=farmacia)
        if form.is_valid():
            form.save()
            return redirect('farmacia_list')
    else:
        form = FarmaciaForm(instance=farmacia)
    return render(request, 'farmacia_form.html', {'form': form})

def farmacia_delete(request, pk):
    farmacia = get_object_or_404(Farmacia, pk=pk)
    if request.method == 'POST':
        farmacia.delete()
        return redirect('farmacia_list')
    return render(request, 'farmacia_delete.html', {'farmacia': farmacia})

# ========== MOTO ==========

def moto_list(request):
    motos = Moto.objects.all()
    return render(request, 'moto_list.html', {'motos': motos})


def moto_create(request):
    if request.method == 'POST':
        form = MotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moto_list')
    else:
        form = MotoForm()
    return render(request, 'moto_form.html', {'form': form})


def moto_update(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        form = MotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            return redirect('moto_list')
    else:
        form = MotoForm(instance=moto)
    return render(request, 'moto_form.html', {'form': form})

def moto_delete(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        moto.delete()
        return redirect('moto_list')
    return render(request, 'moto_delete.html', {'moto': moto})

# ========== MOTORISTA ==========
def motorista_list(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motorista_list.html', {'motoristas': motoristas})

def motorista_create(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('motorista_list')
    else:
        form = MotoristaForm()
    return render(request, 'motorista_form.html', {'form': form})

def motorista_update(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            form.save()
            return redirect('motorista_list')
    else:
        form = MotoristaForm(instance=motorista)
    return render(request, 'motorista_form.html', {'form': form})

def motorista_delete(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        motorista.delete()
        return redirect('motorista_list')
    return render(request, 'motorista_delete.html', {'motorista': motorista})