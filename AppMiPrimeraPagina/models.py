from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
   

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    matricula = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.matricula})"

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10, unique=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    


