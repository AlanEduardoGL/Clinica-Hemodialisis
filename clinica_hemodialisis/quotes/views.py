from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from .forms import FormQuotes
from django.contrib.auth.decorators import login_required
# Realiza transacciones seguras en las consultas ORM.
from django.db import transaction
from django.contrib import messages  # Mensajes de alerta para el usuario.
from django.contrib.auth import get_user_model

# Create your views here.


@login_required # ! Requerimos la sesion al usuario.
def quotes(request):

    # Variable Nula.
    error_message = None
    
    # Instanciamos la clase FormQuotes().
    form = FormQuotes()

    # Validamos que el formulario sea valido.
    if form.is_valid():
        # Recuperamos datos del formulario.
        medic = form.cleaned_data['medic']
        patient = form.cleaned_data['patient']
        date = form.cleaned_data['date']
        symptoms = form.cleaned_data['symptoms']

    return render(request, 'quotes/quotes.html', {'form': form, 'error_message': error_message})


@login_required # ! Requerimos la sesion al usuario.
def add_medicines_quotes(request):

    error_message = None

    return render(request, 'quotes/add_medicines_quotes.html', {'error_message': error_message})


@login_required # ! Requerimos la sesion al usuario.
def summary_quote(request):

    error_message = None

    if request.method == 'POST':
        form = FormQuotes(request.POST)
    else:
        form = FormQuotes()

    return render(request, 'quotes/summary_quote.html', {'error_message': error_message, 'form': form})