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



# --- Cargar dataset global ---
ruta_ia = os.path.join(settings.BASE_DIR, 'netflix_app', 'ia')
df = pd.read_csv(os.path.join(ruta_ia, 'df_movies.csv'))

# --- Vista para mostrar todas las películas ---
def lista_peliculas(request):
    peliculas = df[['titulo']].reset_index().to_dict(orient='records')
    return render(request, 'netflix_app/lista_peliculas.html', {'peliculas': peliculas})

# --- Vista para mostrar detalles de una película ---
def detalle_pelicula(request, id):
    if id < 0 or id >= len(df):
        return render(request, 'netflix_app/detalle_pelicula.html', {'error': 'Película no encontrada.'})

    pelicula = df.iloc[id].to_dict()

    # Opcional: recomendaciones relacionadas
    recomendaciones = recomendar_peliculas(pelicula['title'], 5)

    return render(request, 'netflix_app/detalle_pelicula.html', {
        'pelicula': pelicula,
        'recomendaciones': recomendaciones
    })

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

