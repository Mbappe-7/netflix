from django.db import models


# ---------------- PELÍCULAS ----------------
class Pelicula(models.Model):
    show_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200, blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=20, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    listed_in = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)

    def __str__(self):
        return self.title


# ---------------- SERIES ----------------
class Serie(models.Model):
    show_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200, blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=20, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    listed_in = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)

    def __str__(self):
        return self.title


# ---------------- CONSULTAS (Predicciones IA) ----------------
class Consulta(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=200, blank=True, null=True)
    reparto = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    fecha_lanzamiento = models.IntegerField(blank=True, null=True)
    duracion = models.CharField(max_length=50, blank=True, null=True)
    categorias = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    resultado_prediccion = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta: {self.titulo} ({self.resultado_prediccion or 'Pendiente'})"
