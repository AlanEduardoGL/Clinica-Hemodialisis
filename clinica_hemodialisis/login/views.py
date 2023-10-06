from django.shortcuts import (
    render,
    redirect
)
from .forms import FormLogin
from django.contrib.auth.hashers import check_password
from register.models import User
from django.contrib.auth import (
    login as auth_login, 
    authenticate, 
    logout
) 

# Create your views here.


def login_user(request):
    """
    Vista que maneja el proceso de inicio de sesión, 
    valida las credenciales del usuario y redirige al usuario
    a la página principal si las credenciales son correctas, 
    o muestra un mensaje de advertencia si las credenciales 
    son incorrectas o no existe un usuario con el correo 
    electrónico proporcionado.

    Args:
        request (): _description_

    Returns:
        redirect: Redirecciona al index principal.
        render: Renderiza la plantilla HTML.
    """
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
                    # Iniciamos sesión al usuario.
                    auth_login(request, user)
                    # Validamos la autenticación.
                    if request.user.is_authenticated:
                        # Redirigimos al index principal.
                        return redirect('index')
                    else:
                        warning_message = "El usuario no está autenticado. Intenta nuevamente."
                else:
                    warning_message = f'El correo y/o contraseña ingresados son incorrectos. Intenta nuevamente.'
            except User.DoesNotExist:
                warning_message = f'No hay usuario registrado con el correo "{email}". Intenta nuevamente.'

    else:
        # Instanciamos nuestro formulario.
        form = FormLogin()

    return render(request, 'login/login.html', {'form': form, 'warning_message': warning_message})


def logout_user(request):
    """
    Vista se encarga de cerrar la sesión de un usuario eliminando 
    todas las claves y valores de la sesión y luego redirige al usuario 
    a la página principal de la aplicación. Esto garantiza que el usuario 
    esté completamente cerrado de la sesión y ya no esté autenticado.

    Args:
        request (_type_): _description_

    Returns:
        redirect: Redirige al index principal.
    """
    # Cerramos la sesión del usuario.
    logout(request)

    return redirect('index')
