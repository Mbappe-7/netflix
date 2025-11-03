from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Serie, Consulta
from .forms import PeliculaForm, SerieForm, ConsultaForm

# ---------------- HOME ----------------
def home(request):
    return render(request, 'netflix_app/home.html')


# ---------------- PELÍCULAS ----------------
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'netflix_app/lista_peliculas.html', {'peliculas': peliculas})


def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('netflix_app:lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'netflix_app/crear_pelicula.html', {'form': form, 'accion': 'Crear'})

def detalle_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'netflix_app/detalle_pelicula.html', {'pelicula': pelicula})

def editar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            
            return redirect('netflix_app:lista_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'netflix_app/editar_pelicula.html', {'form': form, 'accion': 'Editar','pelicula': pelicula})
    

def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    return redirect('netflix_app:lista_peliculas')


# ---------------- SERIES ----------------
def lista_series(request):
    series = Serie.objects.all()
    return render(request, 'netflix_app/lista_series.html', {'series': series})

def agregar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('netflix_app:lista_series')
    else:
        form = SerieForm()
    return render(request, 'netflix_app/editar_serie.html', {'form': form, 'accion': 'Agregar'})


def editar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    if request.method == 'POST':
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('netflix_app:lista_series')
    else:
        form = SerieForm(instance=serie)
    return render(request, 'netflix_app/editar_serie.html', {'form': form, 'accion': 'Editar'})

def eliminar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    serie.delete()
    return redirect('netflix_app:lista_series')

def detalle_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    return render(request, 'netflix_app/detalle_serie.html', {'serie': serie})



# ---------------- CONSULTAS ----------------
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'netflix_app/lista_consultas.html', {'consultas': consultas})

def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('netflix_app:lista_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'netflix_app/editar_consulta.html', {'form': form, 'accion': 'Editar'})

def eliminar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    consulta.delete()
    return redirect('netflix_app:lista_consultas')
