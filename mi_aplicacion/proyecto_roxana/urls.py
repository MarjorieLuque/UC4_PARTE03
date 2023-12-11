from django.contrib import admin
from django.urls import path, include
from mi_aplicacion.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_aplicacion/', include('mi_aplicacion.urls')),
    path('', include('mi_aplicacion.urls')),  # Añade esta línea para manejar la URL raíz

]
