from django.urls import path
from . import views

app_name = "netflix_app"
urlpatterns = [
    path('', views.home, name='home'),
    path('consulta/', views.formulario_consulta, name='formulario_consulta'),
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/<int:id>/', views.detalle_pelicula, name='detalle_pelicula'),

    # CONSULTAS IA
    path('consulta/', views.formulario_consulta, name='formulario_consulta'),

]
