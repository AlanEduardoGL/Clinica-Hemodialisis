from django.shortcuts import (
    render, 
    redirect
)
from .forms import FormLogin
from django.contrib.auth.hashers import check_password
from register.models import User

# Create your views here.


def login(request):   

    warning_message = None 

    # Validamos si el usuario envio el formulario.
    if request.method == 'POST':

        # Instanciamos nuestro formulario con peticion POST.
        form = FormLogin(request.POST)

        # Validamos que los campos sean correctos.
        if form.is_valid():

            # Recuperamos datos del formulario.
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # Buscamos el usuario por su correo electrónico.
                user = User.objects.get(email=email)
                
                # Validamos el email y la contraseña.
                if email == user.email and check_password(password, user.password):

                    # Limpiamos cualquier sesion existente.
                    # ! session.clear()

                    # La contraseña es válida, permite el inicio de sesión.
                    return redirect('index')
                
                else:
                    warning_message = f'El correo y/o contraseña ingresados son incorrectos.. Intenta nuevamente.'

            except User.DoesNotExist:
                warning_message = f'No hay usuario registrado con el correo "{email}". Intenta nuevamente.'

    else:
        # Instanciamos nuestro formulario.
        form = FormLogin()

    return render(request, 'login/login.html', {
        'form': form,
        'warning_message': warning_message
    })
