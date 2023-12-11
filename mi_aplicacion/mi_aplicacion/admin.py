# mi_aplicacion/admin.py
from django.contrib import admin
from .models import Course, Career

# Configuración del ModelAdmin para Curso
class CourseAdmin(admin.ModelAdmin):
    list_display = ('idcourse', 'code', 'name', 'hour', 'credits', 'state')
    list_filter = ('state',)
    search_fields = ('code', 'name')

# Configuración del ModelAdmin para Carrera
class CareerAdmin(admin.ModelAdmin):
    list_display = ('idcareer', 'name', 'shortname', 'image', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'shortname')

# Registrar los ModelAdmin en el sitio de administración
admin.site.register(Course, CourseAdmin)
admin.site.register(Career, CareerAdmin)


