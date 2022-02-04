from django.http import HttpResponse
from datetime import datetime

def saludo(request):
	return HttpResponse ("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<h1>Hola!</h1></br><p>Recuerden que esa es mi segunda vista</p>")

def dia_de_hoy(request):
    dia = datetime.now()
    texto = f"<h1>Hola!</h1></br><p>Recuerden que hoy es {dia}</p>"
    return HttpResponse(texto)

def mi_nombre(request, nombre):
    texto = f"<h1>Hola!</h1></br><p>La persona conectada es {nombre}</p>"
    return HttpResponse(texto)

