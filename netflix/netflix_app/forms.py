from django import forms
from .models import Pelicula, Serie, Consulta


# ---------------- PELÍCULAS ----------------
class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = [
            "show_id",
            "title",
            "director",
            "cast",
            "country",
            "date_added",
            "release_year",
            "rating",
            "duration",
            "listed_in",
            "description",
            "poster",
        ]


# ---------------- SERIES ----------------
class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = [
            "show_id",
            "title",
            "director",
            "cast",
            "country",
            "date_added",
            "release_year",
            "rating",
            "duration",
            "listed_in",
            "description",
            "poster",
        ]


# ---------------- CONSULTAS ----------------
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            "titulo",
            "director",
            "reparto",
            "pais",
            "fecha_lanzamiento",
            "duracion",
            "categorias",
            "descripcion",
        ]
