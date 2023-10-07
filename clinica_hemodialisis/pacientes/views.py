from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth.decorators import login_required
from .forms import FormPatient
from .models import Patient
from django.db import transaction # Realiza transacciones seguras en las consultas ORM.
from django.db.models import Q
from django.contrib import messages # Mensajes de alerta para el usuario.
from django.contrib.auth import get_user_model # Realizamos instancias de los modelos.

# Create your views here.


@login_required # ! Requerimos la sesion del usuario.
def agregar_paciente(request):

    error_message = None

    if request.method == 'POST':
        form = FormPatient(request.POST)

        # Validamos que el formulario sea valido.
        if form.is_valid():
            # Recupermaos datos del formulario.
            patient_name = form.cleaned_data['patient_name']
            patient_last_name = form.cleaned_data['patient_last_name']
            patient_age = form.cleaned_data['patient_age']
            gender = form.cleaned_data['gender']
            cell_number = form.cleaned_data['cell_number']
            email = form.cleaned_data['email']
            allergies = form.cleaned_data['allergies']
            symptoms = form.cleaned_data['symptoms']
            street_address = form.cleaned_data['street_address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postal_code = form.cleaned_data['postal_code']

            # Query para buscar coincidencias en el email o cell_number del paciente.
            existing_patient = Patient.objects.filter(
                Q(email=email) | Q(cell_number=cell_number)
            ).exists()

            # Validamos si existe el paciente.
            if existing_patient:
                error_message = f'El paciente "{patient_name}" ya se encuentra registrado. Intenta nuevamente.'
            else:
                try:
                    # Abrimos transaccion.
                    with transaction.atomic():
                        # Realizamos una instancia de User.
                        User = get_user_model()

                        # Obtenemos el ID del usuario logueado de la sesion. 
                        id_user = request.user.id_user

                        # Obtén la instancia de User correspondiente al ID obtenido.
                        user_instance = User.objects.get(id_user=id_user)

                        # Importamos datos a la base de datos.
                        new_patient = Patient.objects.create(
                            id_username=user_instance,
                            patient_name=patient_name,
                            patient_last_name=patient_last_name,
                            patient_age=patient_age,
                            gender=gender,
                            cell_number=cell_number,
                            email=email,
                            allergies=allergies,
                            symptoms=symptoms,
                            street_address=street_address,
                            city=city,
                            state=state,
                            postal_code=postal_code
                        )
                except Exception as e:
                    error_message = f'Error al registrar el paciente "{patient_name}": {str(e)}'
                else:
                    messages.success(request, f'El paciente "{patient_name}" se ha registrado exitosamente.')

                    return redirect('pacientes')
    else:
        form = FormPatient()

    return render(request, 'pacientes/agregar_paciente.html', {'form': form, 'error_message': error_message})


@login_required # ! Requerimos la sesion del usuario. 
def pacientes(request):
    user_patients = None
    error_message = None

    try:
        # Abrimos transaccion.
        with transaction.atomic():
            # Realizamos una instancia de User.
            User = get_user_model()

            # Obtenemos el ID del usuario logueado de la sesion. 
            id_user = request.user.id_user

            # Obtén la instancia de User correspondiente al ID obtenido.
            user = User.objects.get(id_user=id_user)

            # Obtenemos pacientes registrados por el usuario.
            user_patients = Patient.objects.filter(id_username=id_user)

    except Exception as e:
        error_message = f'Ocurrio un error interno al obtener el registro de pacientes. "{str(e)}"'
    else:
        return render(request, 'pacientes/pacientes.html', {'user_patients': user_patients, 'user': user, 'error_message': error_message})
