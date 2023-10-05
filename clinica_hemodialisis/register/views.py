from django.shortcuts import (
    render,
    redirect
)
from .forms import FormRegister
from .models import User
from django.contrib.auth.hashers import (
    make_password,
    check_password
)
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages

# Create your views here.

def register(request):
    """
    Vista que se encarga de manejar el registro de usuarios.

    Args:
        request (): Toma una solicitud HTTP.

    Returns:
        redirect('login): Redirige al usuario para iniciar sesion.
        render('register/register.html): Rendereiza la plantilla HTML.
        error_message: Muestra mensajes de error.
        messages.success: Muestra mensaje de exito.
    """

    error_message = None

    if request.method == 'POST':
        form = FormRegister(request.POST)

        # Validamos que el formulario sea valido.
        if form.is_valid():

            # Recupermaos datos del formulario.
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            cell_number = form.cleaned_data['cell_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            administrator_profile = form.cleaned_data['administrator_profile']

            # Validamos que ambos passwords coinciden.
            if password == confirm_password:

                # Query para buscar email ingresado.
                existing_user = User.objects.filter(email=email).exists()

                # Validamos que el usuario a registrar no exusta en la base de datos.
                if existing_user:
                    error_message = f'El correo "{email}" ya se encuentra registrado. Intenta nuevamente.'
                else:
                    try:
                        # Validamos el password según las políticas de seguridad
                        validate_password(password)

                        # Ciframos el password.
                        hashed_password = make_password(password)

                        # Abrimos transaccion.
                        with transaction.atomic():
                            # Importamos datos a la base de datos.
                            new_user = User.objects.create(
                                username=username,
                                name=name,
                                last_name=last_name,
                                cell_number=cell_number,
                                email=email,
                                password=hashed_password,
                                age=age,
                                administrator_profile=administrator_profile
                            )
                    except Exception as e:
                        error_message = f'Error al crear el usuario "{username}": {str(e)}'
                    else:

                        return redirect('login')

            else:
                error_message = "Las contraseñas no coinciden. Vuelve a intentarlo."
    else:
        form = FormRegister()

    return render(request, 'register/register.html', {
        'form': form,
        'error_message': error_message
    })
