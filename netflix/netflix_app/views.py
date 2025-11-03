from django.shortcuts import render

def home(request):
    return render(request, 'netflix_app/home.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Serie, Consulta
from .forms import PeliculaForm, SerieForm, ConsultaForm

# --------- PELÍCULAS ---------
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/lista.html', {'peliculas': peliculas})

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/form.html', {'form': form, 'accion': 'Agregar'})

def editar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    return redirect('lista_peliculas')


# --------- SERIES ---------
def lista_series(request):
    series = Serie.objects.all()
    return render(request, 'series/lista.html', {'series': series})

def agregar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_series')
    else:
        form = SerieForm()
    return render(request, 'series/form.html', {'form': form, 'accion': 'Agregar'})

def editar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    if request.method == 'POST':
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('lista_series')
    else:
        form = SerieForm(instance=serie)
    return render(request, 'series/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    serie.delete()
    return redirect('lista_series')


# --------- CONSULTAS ---------
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/lista.html', {'consultas': consultas})

def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consultas/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    consulta.delete()
    return redirect('lista_consultas')
