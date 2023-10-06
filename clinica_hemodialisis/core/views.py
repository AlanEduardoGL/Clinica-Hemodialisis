from django.shortcuts import render
from register.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    """
    Vista verifica si un usuario está autenticado y, 
    en caso afirmativo, recupera los datos del usuario 
    para mostrarlos en la página. Si el usuario no está autenticado, 
    muestra un mensaje de advertencia. 
    Esta vista se utiliza para la página de inicio de la aplicación.

    Args:
        request (_type_): _description_

    Returns:
        render: Renderiza la plantilla HTML.
    """
    warning_message = None
    user = None

    if request.user.is_authenticated:
        # Recuperamos el id del usuario de la sesion del objeto "request.user".  
        id_user = request.user.id_user
    else:
        id_user = None

    # Validamos si hay una sesión activa.
    if id_user is not None:
        # Query para traer datos del usuario.
        user = User.objects.get(id_user=id_user)
    else:
        warning_message = f'El usuario no ha iniciado sesión o la sesión ha expirado.'

    return render(request, 'core/index.html', {'warning_message': warning_message, 'user': user})
