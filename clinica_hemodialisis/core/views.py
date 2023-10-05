from django.shortcuts import render
from register.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


# ! Decorador para requerir la sesion del usuario.
# @login_required
def index(request):
    
    warning_message = None
    user = None

    # Recupermos el id del usuario.
    id_user = request.session.get('id_user', None)

    # Validamos si hay una sesión activa.
    if id_user is not None:
        # Query para traer datos del usuario.
        user = User.objects.get(id_user=id_user)

    else:
        warning_message = f'El usuario no ha iniciado sesión o la sesión ha expirado.'

    return render(request, 'core/index.html', {'warning_message': warning_message, 'user': user})
