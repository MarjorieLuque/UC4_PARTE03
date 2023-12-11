from django.urls import path
from .views import cursos, crear_curso, carreras, crear_carrera, index

urlpatterns = [
    path('cursos/', cursos, name='cursos'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('carreras/', carreras, name='carreras'),
    path('crear_carrera/', crear_carrera, name='crear_carrera'),
    path('', index, name='index'),  # Importa la función index
    # ... otras rutas de la aplicación ...
]
