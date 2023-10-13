from django.shortcuts import (
    render,
    redirect
)
from .forms import FormMedicine
# Realiza transacciones seguras en las consultas ORM.
from django.db import transaction
from .models import Medicine
# Mensajes de alerta para el usuario.
from django.contrib import messages

# Create your views here.


def medicines(request):

    # Variables nulas.
    medicines = None
    message_error = None

    # Abrimos excepcion.
    try:
        # Abrimos transaccion.
        with transaction.atomic():
            # Query para obtener todos los medicamentos.
            medicines = Medicine.objects.all()
    except Exception as e:
        # Mensaje de error en caso de excepcion.
        message_error = f'Error al obtener los medicamentos en stock. {str(e)}'
    
    return render(request, 'medicamentos/medicines.html', {'medicines': medicines, 'message_error': message_error})


def add_medicines(request):

    # Variable nula.
    error_message = None

    # Validamos si el usuario envio el formualario por POST.
    if request.method == 'POST':
        # Envio el formulario.
        form = FormMedicine(request.POST)

        # Validamos que el formulario sea valido.
        if form.is_valid():
            # Recuperamos datos del formulario.
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            stock = form.cleaned_data['stock']
            expiration_date = form.cleaned_data['expiration_date']
            category = form.cleaned_data['category']
            
            # Iniciamos excepcione.
            try:
                # Iniciamos transaccion para importar de manera segura en la base de datos.
                with transaction.atomic():
                    # Importamos datos a la base de datos.
                    new_medicine = Medicine.objects.create(
                        name=name,
                        description=description,
                        price=price,
                        stock=stock,
                        expiration_date=expiration_date,
                        category=category
                    )
            except Exception as e:
                error_message = f'Error al registrar el medicamento: "{name}". {str(e)}'
            else:
                messages.success(
                    request,
                    f'Se registro correctamente el medicamento "{name}".'
                )

                return redirect('medicines')
        
    else:
        # Realizamos instancia de la clase.
        form = FormMedicine()
        
    return render(request, 'medicamentos/add_medicines.html', {'form': form, 'error_message': error_message})