from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from .forms import FormMedicine
# Realiza transacciones seguras en las consultas ORM.
from django.db import transaction
from .models import Medicine
# Mensajes de alerta para el usuario.
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required  # ! Requerimos la sesion del usuario.
def medicines(request):
    """
    Vista que verifica si el usuario ha iniciado sesión, 
    recupera una lista de medicamentos de la base de datos 
    y muestra esta lista en una página web. En caso de error, 
    también maneja mensajes de error.

    Args:
        request (HttpRequest): La solicitud web actual.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

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


@login_required  # ! Requerimos la sesion del usuario.
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

            # Iniciamos excepcion.
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


@login_required  # ! Requerimos la sesion del usuario.
def edit_medicine(request, id_medicine):
    """
    Vista que permite a los usuarios agregar nuevos medicamentos 
    a la base de datos, validando los datos ingresados en un formulario 
    y manejando excepciones en caso de errores.

    Args:
        request (HttpRequest): La solicitud web actual.
        id_medicine (int): ID del medicamento a editar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

    # Variables nulas.
    error_message = None
    medicine = None

    # Validamos si envio el formulario.
    if request.method == 'POST':
        # Recuperamos el formulario por POST.
        form = FormMedicine(request.POST)

        # Validamos que el fomrulario sea valido.
        if form.is_valid():
            # Recuperamos datos del formulario.
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            stock = form.cleaned_data['stock']
            expiration_date = form.cleaned_data['expiration_date']
            category = form.cleaned_data['category']
            brand = form.cleaned_data['brand']
            supplier = form.cleaned_data['supplier']

            # Abrimos excepcion.
            try:
                # Abrimos transaccion.
                with transaction.atomic():
                    # Query para recuperar el medicamento a editar/actualizar por su ID.
                    update_medicine = Medicine.objects.get(id=id_medicine)

                    # Actualizamos los nuevos datos del medicamento en el modelo Medicine.
                    update_medicine.name = name
                    update_medicine.description = description
                    update_medicine.price = price
                    update_medicine.stock = stock
                    update_medicine.expiration_date = expiration_date
                    update_medicine.category = category
                    update_medicine.brand = brand
                    update_medicine.supplier = supplier

                    # Guardamos los cambios.
                    update_medicine.save()
            except Exception as e:
                error_message = f'Error al actualizar datos. Intenta nuevamente. {str(e)}'
            else:
                # Mensaje de exito para el usuario.
                messages.success(
                    request,
                    f'Se actualizo correctamente el medicamento "{name}".'
                )
                # Redirigimos al usuario.
                return redirect('medicines')
    else:
        # Abrimos excepcion.
        try:
            # Abrimos transacion.
            with transaction.atomic():
                # Buscamos al medicamento utilizando get_object_or_404 para manejar casos de no existencia.
                medicine = get_object_or_404(Medicine, id=id_medicine)
        except Exception as e:
            error_message = f'El medicamento con ID "{id_medicine}" no fue encontrado: {str(e)}'

        # Creamos una instancia del formulario y establecemos el valor inicial de los campos.
        form = FormMedicine(initial={
            'name': medicine.name,
            'description': medicine.description,
            'price': medicine.price,
            'stock': medicine.stock,
            'expiration_date': medicine.expiration_date,
            'category': medicine.category,
            'brand': medicine.brand,
            'supplier': medicine.supplier
        })

    return render(request, 'medicamentos/edit_medicine.html', {'form': form, 'error_message': error_message, 'medicine': medicine})


@login_required  # ! Requerimos la sesion del usuario.
def confirm_delete_medicine(request, id_medicine):
    """
    Vista que se utiliza para mostrar información sobre un medicamento específico 
    y confirmar su eliminación. Si el medicamento se encuentra en la base de datos, 
    se mostrará en la plantilla junto con la opción de confirmar la eliminación. 
    Si ocurre algún error, se mostrará un mensaje de error.

    Args:
        request (HttpRequest): La solicitud web actual.
        id_medicine (int): ID del medicamento a editar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

    # Variables nulas.
    message_error = None
    medicine = None

    # Abrimos excepcion.
    try:
        # Abrimos transaccion.
        with transaction.atomic():
            # Query para traer el medicamento por su ID.
            medicine = Medicine.objects.get(id=id_medicine)
    except Exception as e:
        # Mandamos mensaje de error en caso de excepcion.
        message_error = f'Error interno. Intenta nuevamente. {str(e)}.'

    return render(request, 'medicamentos/confirm_delete_medicine.html', {'message_error': message_error, 'medicine': medicine})


@login_required  # ! Requerimos la sesion del usuario.
def delete_medicine(request, id_medicine):
    """
    Vista que se utiliza para eliminar un medicamento específico de la base de datos. 
    Si la eliminación es exitosa, se muestra un mensaje de éxito y se redirige 
    a la vista de lista de medicamentos. Si ocurre algún error, se muestra un mensaje de error.

    Args:
        request (HttpRequest): La solicitud web actual.
        id_medicine (int): ID del medicamento a editar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el resultado.
    """

    # Variable nula.
    error_message = None

    # Abrimos excepcion.
    try:
        # Abrimos transaccion.
        with transaction.atomic():
            # Query para obtener el paciente a eliminar.
            delete_medicine = Medicine.objects.get(id=id_medicine)
            # Eliminamos el registro.
            delete_medicine.delete()
    except Exception as e:
        # Mensaje de error al usuario.
        error_message = f'Error al eliminar el medicamento "{delete_medicine.name}". {str(e)}'

        return render(request, 'medicamentos/confirm_delete_medicine.html', {'error_message': error_message})
    else:
        # Mensaje de exito al usuario.
        messages.success(
            request,
            f'Se elimino con exito el medicamento "{delete_medicine.name}"'
        )

        return redirect('medicines')
