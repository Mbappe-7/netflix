from django.contrib import admin
from .models import Pelicula, Serie, Consulta

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'release_year', 'rating')
    search_fields = ('title', 'country', 'listed_in')

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'release_year', 'rating')
    search_fields = ('title', 'country', 'listed_in')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pais', 'fecha_lanzamiento', 'resultado_prediccion', 'fecha_creacion')
    search_fields = ('titulo', 'pais', 'categorias')
