from django.shortcuts import render, redirect
from .forms import FormQuotes
from .models import Quotes
# Realiza transacciones seguras en las consultas ORM.
from django.db import transaction
# Mensajes de alerta para el usuario.
from django.contrib import messages

# Create your views here.


def quotes(request):

    error_message = None

    # Validmaos que el usuario envió el formulario por POST.
    if request.method == 'POST':
        
        form = FormQuotes(request.POST)

        # Validamos el formulario.
        if form.is_valid():
            # Recuperamos los datos del fomulario.
            medic = form.cleaned_data['medic'];
            patient = form.cleaned_data['patient'];
            date = form.cleaned_data['date'];
            symptoms = form.cleaned_data['symptoms'];
            medicines = form.cleaned_data['medicines'];
            total_price = form.cleaned_data['total_price'];
    
            # Iniciamos transacción.
            try:
                # Iniciamos transaccion para importar de manera segura en la base de datos.
                with transaction.atomic():
                    # Importamos datos a la base de datos.
                    new_quote = Quotes.objects.create(
                        medic = medic,
                        patient = patient,
                        date = date,
                        symptoms = symptoms,
                        total_price = total_price
                    )

                    new_quote.medicines.set(medicines)
            except Exception as e:
                error_message = f'Error al registrar la cita para: "{patient}". {str(e)}'
            else:
                messages.success(
                    request,
                    f'Se registro correctamente la cita para "{patient}".'
                )

                return redirect('index')
    else:
        form = FormQuotes()

    return render(request, 'quotes/quotes.html', {'form': form, 'error_message': error_message})
