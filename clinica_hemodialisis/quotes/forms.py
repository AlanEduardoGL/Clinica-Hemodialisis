from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import CharField
from django.db.models.functions import Concat
from django.db.models import F, Value
from register.models import User
from pacientes.models import Patient
from medicamentos.models import Medicine


Quotes = get_user_model()


class FloatInput(forms.TextInput):
    input_type = 'number'


class FormQuotes(forms.Form):
    medic = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset = User.objects.all(),
=======
        queryset=User.objects.all().annotate(
            full_name_medic=Concat(F('last_name'), Value(' '), F('name'))
        ),
>>>>>>> 1cba098d56860c78bec18d20d025fba65f5a0e8b
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'medic',
            'placeholder': 'Medico'
        }),
        empty_label="Selecciona una médico"
    )
    patient = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset = Patient.objects.all(),  # Asegúrate de importar el modelo Patient
=======
        queryset=Patient.objects.all().annotate(
            full_name_patient=Concat(
                F('patient_last_name'), Value(' '), F('patient_name'))
        ),
>>>>>>> 1cba098d56860c78bec18d20d025fba65f5a0e8b
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'patient',
            'placeholder': 'Paciente'
        }),
        empty_label="Selecciona un paciente"
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

    # Configuramos los "label" de cada input.
    def __init__(self, *args, **kwargs):
        super(FormQuotes, self).__init__(*args, **kwargs)
        self.fields['medic'].label = "Médico"
        self.fields['patient'].label = "Paciente"
        self.fields['date'].label = "Fecha de Cita"
        self.fields['symptoms'].label = "Síntomas"
