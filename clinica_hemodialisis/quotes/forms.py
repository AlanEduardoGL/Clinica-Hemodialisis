from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from pacientes.models import Patient
from medicamentos.models import Medicine
from register.models import User

Quotes = get_user_model()

class FloatInput(forms.TextInput):
    input_type = 'number'

class FormQuotes(forms.Form):
    medic = forms.ModelChoiceField(
        queryset = User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'medic',
            'placeholder': 'Medico'
        })
    )
    patient = forms.ModelChoiceField(
        queryset = Patient.objects.all(),  # Asegúrate de importar el modelo Patient
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'patient',
            'placeholder': 'Paciente'
        })
    )
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'name': 'date',
        'placeholder': 'Fecha de Cita',
        'type': 'date'
    }))
    symptoms = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'symptoms',
        'placeholder': 'Síntomas'
    }))
    medicines = forms.ModelMultipleChoiceField(
        queryset = Medicine.objects.all(),  # Asegúrate de importar el modelo Medicine
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
            'name': 'medicines',
            'placeholder': 'Medicamento'
        })
    )
    total_price = forms.FloatField(widget=FloatInput(attrs={
        'class': 'form-control',
        'name': 'total_price',
        'placeholder': 'Precio Total'
    }))
