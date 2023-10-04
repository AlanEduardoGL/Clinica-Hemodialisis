from django.shortcuts import render

# Create your views here.


def pacientes_registrados(request):

    return render(request, 'pacientes/pacientes.html')