from django.shortcuts import render
from eventos.models import Certificado, Evento

def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})

def meus_eventos(request):
    logos = Evento.objects.filter(criador=request.user)
    return render(request, 'meus_eventos.html', {'logos': logos})
