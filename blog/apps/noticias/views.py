from django.shortcuts import render
from .models import Noticia
# Create your views here.
def ListarNoticias(request):
    contexto = {} #diccionario

    n = Noticia.objects.all() #SELECT * FROM Noticias

    contexto['noticias'] = n

    return render(request, 'noticias/listar.html', contexto)