from django.shortcuts import (
    render,
    redirect
)
from .forms import FormLogin
from django.contrib.auth.hashers import check_password
from register.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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
                    # Limpiamos cualquer sesion existente.
                    request.session.clear()
                    # Guardamos el id del usuario en la sesion.
                    request.session['id_user'] = user.id_user
                    # Redirigimos al index principal.
                    return redirect('index')
                else:
                    warning_message = f'El correo y/o contraseña ingresados son incorrectos. Intenta nuevamente.'
                    
            except User.DoesNotExist:
                warning_message = f'No hay usuario registrado con el correo "{email}". Intenta nuevamente.'

    else:
        # Instanciamos nuestro formulario.
        form = FormLogin()

    return render(request, 'login/login.html', {
        'form': form,
        'warning_message': warning_message
    })


@login_required
def logout(request):

    # Elimina la sesión completa (incluyendo todas las claves y valores)
    request.session.flush()

    return redirect('index')
