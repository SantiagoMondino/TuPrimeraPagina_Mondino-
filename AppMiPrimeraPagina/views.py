from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import ProfesorForm, EstudianteForm, CursoForm, BuscarEstudianteForm

def index(request):
    return render(request, 'index.html')

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'agregar_curso.html', {'form': form})

def buscar_estudiante(request):
    estudiantes = None
    matricula_buscada = None
    
    if request.method == 'POST':
        form = BuscarEstudianteForm(request.POST)
        if form.is_valid():
            matricula_buscada = form.cleaned_data['matricula']
            estudiantes = Estudiante.objects.filter(matricula__icontains=matricula_buscada)
    else:
        form = BuscarEstudianteForm()
    
    return render(request, 'buscar_estudiante.html', {
        'form': form,
        'estudiantes': estudiantes,
        'matricula_buscada': matricula_buscada
    })
