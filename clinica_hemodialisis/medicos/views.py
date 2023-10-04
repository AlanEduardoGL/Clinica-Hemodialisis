from django.shortcuts import render

# Create your views here.


def medicos_registrados(request):

    return render(request, 'medicos/medicos.html')