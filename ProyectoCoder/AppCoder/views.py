from django.shortcuts import render

from AppCoder.forms import CursoFormulario
from .models import Curso



# Create your views here.

def curso(request):
    return render (request, 'AppCoder/curso.html')

def inicio (request):
    return render (request, 'AppCoder/index.html')


def curso_formulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_curso = informacion['nombre']
            r_camada = informacion['camada']
        
            curso = Curso(nombre=r_curso, camada=r_camada)
            curso.save()
    
  
    miFormulario = CursoFormulario()
    return render(request, 'AppCoder/curso_formulario.html', {"miFormulario" : miFormulario})



