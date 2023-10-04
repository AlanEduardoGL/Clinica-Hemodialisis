from django.shortcuts import render, redirect
from .forms import FormularioLogin

# Create your views here.


def login(request):    

    if request.method == 'POST':
        form = FormularioLogin(request.POST)

        # Validamos que los campos sean correctos.
        if form.is_valid():

            # Recuperamos datos y guardamos en la base de datos.

            return redirect('')
    
    else:
        # Instanciamos nuestro formulario.
        form = FormularioLogin()

    return render(request, 'login/login.html', {'form': form})
