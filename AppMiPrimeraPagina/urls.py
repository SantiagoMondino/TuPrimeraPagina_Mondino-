from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profesores/nuevo/', views.agregar_profesor, name='agregar_profesor'),
    path('estudiantes/nuevo/', views.agregar_estudiante, name='agregar_estudiante'),
    path('cursos/nuevo/', views.agregar_curso, name='agregar_curso'),
    path('estudiantes/buscar/', views.buscar_estudiante, name='buscar_estudiante'),
]

