from django.shortcuts import (
    render, 
    redirect
)
from django.contrib.auth.decorators import login_required
from .forms import FormPatient
from .models import Patient
from django.db import transaction
from django.db.models import Q

# Create your views here.


@login_required
def pacientes(request):

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
            existing_patient = Patient.objects.filter(Q(email=email) | Q(cell_number=cell_number)).exists()

            # Validamos si existe el paciente
            if existing_patient:
                error_message = f'El paciente "{patient_name}" ya se encuentra registrado. Intenta nuevamente.'
            else:
                try:
                    # Abrimos transaccion.
                    with transaction.atomic():
                        # Importamos datos a la base de datos.
                        new_patient = Patient.objects.create(
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
                    return redirect('login')

    return render(request, 'pacientes/pacientes.html')