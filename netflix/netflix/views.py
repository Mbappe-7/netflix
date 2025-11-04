from django import forms
from .models import Pelicula, Serie, Consulta


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = "__all__"


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = "__all__"


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = "__all__"
