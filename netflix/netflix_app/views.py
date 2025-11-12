from django.shortcuts import render, redirect, get_object_or_404
from .models import Pelicula, Serie, Consulta
from .forms import PeliculaForm, SerieForm, ConsultaForm
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import pandas as pd
import joblib
from django.conf import settings

# 🔹 Rutas a tus archivos
RUTA_IA = os.path.join(settings.BASE_DIR, 'netflix_app', 'ia')
RUTA_CSV = os.path.join(RUTA_IA, 'peliculas_procesadas.csv')
RUTA_MODELO = os.path.join(RUTA_IA, 'modelo_similitud.pkl')
RUTA_VECTORIZER = os.path.join(RUTA_IA, 'vectorizer.pkl')

# 🔹 Cargar archivos una sola vez
df_peliculas = pd.read_csv(RUTA_CSV, encoding='utf-8')
modelo_similitud = joblib.load(RUTA_MODELO)
vectorizer = joblib.load(RUTA_VECTORIZER)

# ---------------- HOME ----------------
def home(request):
    return render(request, "netflix_app/home.html")


# ---------------- PELÍCULAS ----------------
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "netflix_app/lista_peliculas.html", {"peliculas": peliculas})


def crear_pelicula(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("netflix_app:lista_peliculas")
    else:
        form = PeliculaForm()
    return render(
        request, "netflix_app/crear_pelicula.html", {"form": form, "accion": "Crear"}
    )


def detalle_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, "netflix_app/detalle_pelicula.html", {"pelicula": pelicula})


def editar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == "POST":
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()

            return redirect("netflix_app:lista_peliculas")
    else:
        form = PeliculaForm(instance=pelicula)
    return render(
        request,
        "netflix_app/editar_pelicula.html",
        {"form": form, "accion": "Editar", "pelicula": pelicula},
    )


def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    return redirect("netflix_app:lista_peliculas")


# ---------------- SERIES ----------------
def lista_series(request):
    series = Serie.objects.all()
    return render(request, "netflix_app/lista_series.html", {"series": series})


def agregar_serie(request):
    if request.method == "POST":
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("netflix_app:lista_series")
    else:
        form = SerieForm()
    return render(
        request, "netflix_app/editar_serie.html", {"form": form, "accion": "Agregar"}
    )


def editar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    if request.method == "POST":
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect("netflix_app:lista_series")
    else:
        form = SerieForm(instance=serie)
    return render(
        request, "netflix_app/editar_serie.html", {"form": form, "accion": "Editar"}
    )


def eliminar_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    serie.delete()
    return redirect("netflix_app:lista_series")


def detalle_serie(request, id):
    serie = get_object_or_404(Serie, id=id)
    return render(request, "netflix_app/detalle_serie.html", {"serie": serie})


# ---------------- CONSULTAS ----------------


def formulario_consulta(request):
    if request.method == 'POST':
        consulta = request.POST.get('consulta')

        # Obtener la ruta base del proyecto
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ia_path = os.path.join(base_dir, 'ia')

        # Cargar el modelo y el vectorizador con rutas absolutas
        with open(os.path.join(ia_path, '/workspaces/netflix/netflix/netflix_app/ia/modelo_similitud.pkl'), 'rb') as f:
            modelo_similitud = pickle.load(f)
        with open(os.path.join(ia_path, '/workspaces/netflix/netflix/netflix_app/ia/vectorizer.pkl'), 'rb') as f:
            vectorizer = pickle.load(f)

        # Cargar el dataset
        df = pd.read_csv(os.path.join(ia_path, '/workspaces/netflix/netflix/netflix_app/ia/peliculas_procesadas.csv'))

        if not consulta:
            return render(request, '/workspaces/netflix/netflix/netflix_app/templates/netflix_app/formulario_consulta.html', {'error': 'Por favor, escribe una película o género.'})

        # Transformar la consulta y calcular similitudes
        vector_consulta = vectorizer.transform([consulta])
        similitudes = cosine_similarity(vector_consulta, modelo_similitud)[0]
        indices_similares = similitudes.argsort()[-5:][::-1]
        recomendaciones = df.iloc[indices_similares][['titulo', 'genero', 'año', 'duracion', 'director', 'pais', 'calificacion']]

        return render(request, 'consulta.html', {'recomendaciones': recomendaciones.to_dict(orient='records')})

    return render(request, '/workspaces/netflix/netflix/netflix_app/templates/netflix_app/formulario_consulta.html')