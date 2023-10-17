from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

Quotes = get_user_model()

class FloatInput(forms.TextInput):
    input_type = 'number'

class FormQuotes(forms.Form):
    medic = forms.SelectMultiple(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'medic',
        'placeholder': 'Medico'
    }))
    patient = forms.SelectMultiple(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'patient',
        'placeholder': 'Paciente'
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'name': 'date',
        'placeholder': 'Fecha de Cita',
        'type': 'date'  # Esto establece el tipo de entrada como 'date' para un selector de fecha en el navegador.
    }))
    symptoms = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'symptoms',
        'placeholder': 'Síntomas'
    }))
    medicines = forms.SelectMultiple(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'medicines',
        'placeholder': 'Medicamento'
    }))
    total_price = forms.FloatField(widget=FloatInput(attrs={
        'class': 'form-control',
        'name': 'total_price',
        'placeholder': 'Precio Total'
    }))