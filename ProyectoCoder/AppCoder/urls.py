from django.contrib import admin
from django.urls import path
from AppCoder import views
from AppCoder.views import curso, inicio, curso_formulario


urlpatterns = [
    path('curso/', curso, name = "AppCoder Curso"),
    path('inicio/', inicio, name ="AppCoder Inicio"),
    path('cursoformulario/', curso_formulario, name="AppCoderCursoFormulario"),


       
]

