from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .models import Career

def cursos(request):
    cursosListado = Course.objects.all()
    return render(request, 'cursos.html', {"curso": cursosListado})

def crear_curso(request):
    return render(request, 'crear_curso.html', {})

def crear_carrera(request):
    return render(request, 'crear_carrera.html', {})
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Reemplaza 'index.html' con el nombre de tu plantilla
# mi_aplicacion/views.py

def eliminar_curso(request,idcourse):
    curso=Course.objects.get(idcourse=idcourse)
    curso.delete()
    return redirect('/cursos/')

def registrar_curso(request):
    code=request.POST['code']
    name=request.POST['name']
    hour=request.POST['hour']
    credits=request.POST['credits']
    state=request.POST['state']
    curso=Course.objects.create(code=code,name=name,hour=hour,credits=credits,state=state)
    return redirect('/crear_curso/')

def eliminar_carrera(request, idcareer):
    carrera = Career.objects.get(idcareer=idcareer)
    carrera.delete()
    return redirect('/carreras/')

def registrar_carrera(request):
    
    name = request.POST['name']
    shortname = request.POST['shortname']
    image = request.FILES['image']
    state = request.POST['state']

    # Guardar la carrera y su imagen en la carpeta 'media/careers/'
    carrera = Career.objects.create( name=name, shortname=shortname, image=image, state=state)
    
    return redirect('/crear_carrera/')

def carreras(request):
    carrerasListado = Career.objects.all()
    return render(request, 'carreras.html', {"carreras": carrerasListado})
