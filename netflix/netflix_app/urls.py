from django.urls import path
from . import views
app_name = 'netflix_app'
urlpatterns = [
    # PELÍCULAS
    path('', views.home, name='home'),
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/crear/', views.crear_pelicula, name='crear_pelicula'),
    path('peliculas/<int:id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('peliculas/editar/<int:id>/', views.editar_pelicula, name='editar_pelicula'),
    path('peliculas/eliminar/<int:id>/', views.eliminar_pelicula, name='eliminar_pelicula'),

    # SERIES
    path('series/', views.lista_series, name='lista_series'),
    path('series/agregar/', views.editar_serie, name='editar_serie'),
    path('series/editar/<int:id>/', views.editar_serie, name='editar_serie'),
    path('series/eliminar/<int:id>/', views.eliminar_serie, name='eliminar_serie'),
    path('series/<int:id>/', views.detalle_serie, name='detalle_serie'),

    # CONSULTAS IA
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('consultas/editar/<int:id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/eliminar/<int:id>/', views.eliminar_consulta, name='eliminar_consulta'),
]
