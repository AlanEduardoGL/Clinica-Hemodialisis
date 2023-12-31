from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from .forms import FormPatient
from .models import Patient
# Realiza transacciones seguras en las consultas ORM.
from django.db import transaction
from django.db.models import Q
from django.contrib import messages  # Mensajes de alerta para el usuario.
# Realizamos instancias de los modelos.
from django.contrib.auth import get_user_model

# Create your views here.


@login_required  # ! Requerimos la sesion del usuario.
def agregar_paciente(request):
    """
    Vista que se encarga de manejar el proceso de registro de un nuevo paciente, 
    validando los datos ingresados, evitando registros duplicados 
    y mostrando mensajes de éxito o error según corresponda. 
    Además, requiere que el usuario esté autenticado para acceder a ella.

    Args:
        request (HttpRequest): La solicitud web actual.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """
    error_message = None

    if request.method == 'POST':
        # Envio el formulario.
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
                    messages.success(
                        request, 
                        f'El paciente "{patient_name}" se ha registrado exitosamente.'
                    )

                    return redirect('pacientes')
    else:
        form = FormPatient()

    return render(request, 'pacientes/agregar_paciente.html', {'form': form, 'error_message': error_message})


@login_required  # ! Requerimos la sesion del usuario.
def pacientes(request):
    """
    Vista que muestra la lista de pacientes asociados al usuario autenticado. 
    Primero, verifica que el usuario esté autenticado utilizando @login_required, 
    luego obtiene la lista de pacientes y muestra estos datos en la plantilla 
    'pacientes/pacientes.html'. También maneja errores internos y muestra mensajes 
    de error en caso de que ocurran problemas durante el proceso de obtención de datos.

    Args:
        request (HttpRequest): La solicitud web actual.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """
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

    return render(request, 'pacientes/pacientes.html', {'user_patients': user_patients, 'user': user, 'error_message': error_message})


@login_required  # ! Requerimos la sesion del usuario.
def edit_patient(request, id_patient):
    """
    Vista que maneja tanto la visualización inicial de la página de edición 
    como la actualización de los datos del paciente en la base de datos cuando 
    se envía el formulario. Además, gestiona los mensajes de éxito y errores para 
    informar al usuario sobre el resultado de la operación.

    Args:
        request (HttpRequest): La solicitud web actual.
        id_patient (int): ID del usuario a editar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

    error_message = None
    patient = None

    # Validamos si el usuario envio el formualario por POST.
    if request.method == 'POST':
        # Envio el formulario.
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

            try:
                with transaction.atomic():
                    # Obtenemos la instancia del paciente que queremos actualizar/editar.
                    update_patient = Patient.objects.get(id_patient=id_patient)

                    # Actualizamos los nuevos datos del paciente en el modelo Patient.
                    update_patient.patient_name = patient_name
                    update_patient.patient_last_name = patient_last_name
                    update_patient.patient_age = patient_age
                    update_patient.gender = gender
                    update_patient.cell_number = cell_number
                    update_patient.email = email
                    update_patient.allergies = allergies
                    update_patient.symptoms = symptoms
                    update_patient.street_address = street_address
                    update_patient.city = city
                    update_patient.state = state
                    update_patient.postal_code = postal_code

                    # Guardamos los cambios.
                    update_patient.save()
            except Exception as e:
                error_message = f'Error interno al actualizar el paciente {patient_name}: {str(e)}'
            else:
                # Redirigimos al usuario a sus pacientes con mensaje de exito.
                messages.success(
                    request, 
                    f'Se actualizo exitosamente el paciente "{patient_name}".'
                )

                return redirect('pacientes')
        else:
            # Devolver el formulario con los errores
            return render(request, 'pacientes/edit_patient.html', {'error_message': error_message, 'patient': patient, "form": form})
    else:
        # Validamos "id_patient"
        if id_patient:
            try:
                # Abrimos trabsaccion.
                with transaction.atomic():
                    # Buscamos al paciente utilizando get_object_or_404 para manejar casos de no existencia.
                    patient = get_object_or_404(Patient, id_patient=id_patient)
            except Exception as e:
                error_message = f'El paciente con ID "{id_patient}" no fue encontrado: {str(e)}'
        else:
            error_message = 'No se proporcionó un ID de paciente válido.'

        # Creamos una instancia del formulario y establecemos el valor inicial de los campos.
        form = FormPatient(initial={
            'patient_name': patient.patient_name,
            'patient_last_name': patient.patient_last_name,
            'patient_age': patient.patient_age,
            'gender': patient.gender,
            'cell_number': patient.cell_number,
            'email': patient.email,
            'allergies': patient.allergies,
            'symptoms': patient.symptoms,
            'street_address': patient.street_address,
            'city': patient.city,
            'state': patient.state,
            'postal_code': patient.postal_code
        })

    return render(request, 'pacientes/edit_patient.html', {'error_message': error_message, 'patient': patient, "form": form})


@login_required  # ! Requerimos la sesion del usuario.
def confirm_delete_patient(request, id_patient):
    """
    Vista que maneja la confirmación de la eliminación de un paciente. 
    Si todo va bien, muestra los detalles del paciente. Si ocurre algún error, 
    muestra un mensaje de error. El uso de transaction.atomic() 
    garantiza la integridad de la base de datos en caso de errores.

    Args:
        request (HttpRequest): La solicitud web actual.
        id_patient (int): El ID del paciente a eliminar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

    # Variables nulas.
    message_error = None
    patient = None

    try:
        # Abrimos transaccion.
        with transaction.atomic():
            # Query para traer al paciente por su ID.
            patient = Patient.objects.get(id_patient=id_patient)
    except Exception as e:
        # Mandamos mensaje de error en caso de excepcion.
        message_error = f'Error interno. Intenta nuevamente. {str(e)}.'

    return render(request, 'pacientes/confirm_delete_patient.html', {'message_error': message_error, 'patient': patient})



@login_required  # ! Requerimos la sesion del usuario.
def delete_patient(request, id_patient):
    """
    Vista que maneja la eliminación de un paciente. 
    Si la eliminación tiene éxito, muestra un mensaje de éxito 
    al usuario y lo redirige a la página de pacientes. Si ocurre un error, 
    muestra un mensaje de error y redirige al usuario a la página 
    de confirmación de eliminación de paciente. El uso de transaction.atomic() 
    garantiza la integridad de la base de datos en caso de errores.

    Args:
        request (HttpRequest): La solicitud web actual.
        id_patient (int): El ID del paciente a eliminar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

    # Variable nula.
    error_message = None

    try:
        # Abrimos transaccion.
        with transaction.atomic():
            # Query para obtener el paciente a eliminar.
            delete_patient = Patient.objects.get(id_patient=id_patient)
            # Eliminamos el registro.
            delete_patient.delete()
    except Exception as e:
        # Mensaje de error al usuario.
        error_message = f'Error al eliminar el paciente "{delete_patient.patient_name}". {str(e)}'

        return render(request, 'pacientes/confirm_delete_patient.html', {'error_message': error_message})
    else:
        # Mensaje de exito al usuario.
        messages.success(
            request,
            f'Se elimino con exito el usuario "{delete_patient.patient_name}"'
        )

        return redirect('pacientes')
