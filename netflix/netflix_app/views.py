from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Serie, Consulta
from .forms import PeliculaForm, SerieForm, ConsultaForm
import os
import joblib
import pandas as pd
import scipy.sparse as sp
from sklearn.metrics.pairwise import cosine_similarity
from django.conf import settings
from django.shortcuts import render
from .recomendador import recomendar_peliculas


# ---------------- HOME ----------------
def home(request):
    return render(request, "netflix_app/home.html")


# ---------------- PELÍCULAS ----------------

ruta_ia = os.path.join(settings.BASE_DIR, 'netflix_app', 'ia')

# Cargar el dataset
df = pd.read_csv(os.path.join(ruta_ia, 'df_movies.csv'), sep=',')
print("Columnas del dataset:", df.columns.tolist())
print("Primeras filas:\n", df.head())


# --- Cargar dataset global ---
def lista_peliculas(request):
    peliculas = df.reset_index().to_dict(orient='records')
    return render(request, 'netflix_app/lista_peliculas.html', {'peliculas': peliculas})

# --- Vista para mostrar detalles de una película ---
def detalle_pelicula(request, id):
    ruta_ia = os.path.join(settings.BASE_DIR, 'netflix_app', 'ia')
    df = pd.read_csv(os.path.join(ruta_ia, 'df_movies.csv'))

    if id < len(df):
        pelicula = df.iloc[id]
        context = {
            'titulo': pelicula['titulo'],
            'genero': pelicula['genero'],
            'anio': pelicula['aÃ±o'],
            'duracion': pelicula['duracion'],
            'director': pelicula['director'],
            'pais': pelicula['pais'],
        }
    else:
        context = {
            'titulo': 'Película no encontrada',
            'genero': '',
            'anio': '',
            'duracion': '',
            'director': '',
            'pais': '',
        }

    return render(request, 'netflix_app/detalle_pelicula.html', context)

# ---------------- RECOMENDADOR ----------------

from django.shortcuts import render
from .recomendador import recomendar_peliculas

def formulario_consulta(request):
    recomendaciones = []
    titulo_busqueda = ""

    if request.method == "POST":
        titulo_busqueda = request.POST.get("titulo")
        recomendaciones = recomendar_peliculas(titulo_busqueda, 5)

    return render(request, "netflix_app/formulario_consulta.html", {
        "recomendaciones": recomendaciones,
        "titulo_busqueda": titulo_busqueda
    })

