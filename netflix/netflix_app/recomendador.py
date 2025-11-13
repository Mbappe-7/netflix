import pandas as pd
import numpy as np
import joblib
import os
from django.conf import settings

# --- Cargar los archivos desde la carpeta 'ia' ---
ruta_ia = os.path.join(settings.BASE_DIR, 'netflix_app', 'ia')

df = pd.read_csv(os.path.join(ruta_ia, 'df_movies.csv'))
tfidf_vectorizer = joblib.load(os.path.join(ruta_ia, 'tfidf_vectorizer.joblib'))
cosine_sim = joblib.load(os.path.join(ruta_ia, 'cosine_sim.joblib'))


def recomendar_peliculas(titulo, num_recomendaciones=5):
    if titulo not in df['titulo'].values:
        return []

    # Índice del título
    idx = df.index[df['titulo'] == titulo][0]

    # Puntuaciones de similitud
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Quitar la película original
    sim_scores = sim_scores[1:num_recomendaciones+1]

    indices = [i[0] for i in sim_scores]
    similitudes = [round(i[1] * 100, 2) for i in sim_scores]

    recomendaciones = []
    for i, s in zip(indices, similitudes):
        recomendaciones.append({
            'titulo': df['titulo'].iloc[i],
            'similitud': s
        })

    return recomendaciones
