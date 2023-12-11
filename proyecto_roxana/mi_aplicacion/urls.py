from django.urls import path
from .views import cursos, crear_curso, carreras, crear_carrera, index,eliminar_curso,registrar_curso
from .views import eliminar_carrera,registrar_carrera
urlpatterns = [
    path('cursos/', cursos, name='cursos'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('carreras/', carreras, name='carreras'),
    path('crear_carrera/', crear_carrera, name='crear_carrera'),
    path('', index, name='index'),  # Importa la función index
    # ... otras rutas de la aplicación ...
    path('eliminarcurso/<int:idcourse>/',eliminar_curso, name='eliminar_curso'),
    path('registrarCurso/', registrar_curso, name='registrar_curso'),
    # Nuevas rutas para carreras
    path('eliminarcarrera/<int:idcareer>/', eliminar_carrera, name='eliminar_carrera'),
    path('registrarcarrera/', registrar_carrera, name='registrar_carrera'),
]
