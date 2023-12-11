from django.urls import path
from .views import cursos, crear_curso, carreras, crear_carrera, index,eliminar_curso,registrar_curso

urlpatterns = [
    path('cursos/', cursos, name='cursos'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('carreras/', carreras, name='carreras'),
    path('crear_carrera/', crear_carrera, name='crear_carrera'),
    path('', index, name='index'),  # Importa la función index
    # ... otras rutas de la aplicación ...
    path('eliminarcurso/<int:idcourse>/',eliminar_curso, name='eliminar_curso'),
    path('registrarCurso/', registrar_curso, name='registrar_curso'),
    
]
