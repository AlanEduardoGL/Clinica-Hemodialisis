from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

Patient = get_user_model()


class FormPatient(forms.Form):
    patient_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'patient_name',
        'placeholder': 'Nombre del Paciente'
    }))
    patient_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'patient_last_name',
        'placeholder': 'Apellidos del Paciente'
    }))
    patient_age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'patient_age',
        'placeholder': 'Edad'
    }))
    # Agregamos el campo gender
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'name': 'gender',
        }),
        label='Género'
    )
    cell_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'cell_number',
        'placeholder': 'Número de Teléfono'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'name': 'email',
        'placeholder': 'Correo Electrónico'
    }))
    allergies = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'allergies',
        'placeholder': 'Alergias'
    }))
    symptoms = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'symptoms',
        'placeholder': 'Síntomas'
    }))
    street_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'street_address',
        'placeholder': 'Nombre del Paciente'
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'city',
        'placeholder': 'Ciudad'
    }))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'state',
        'placeholder': 'Estado'
    }))
    postal_code = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'postal_code',
        'placeholder': 'Código Postal'
    }))

    def clean_patient(self):
        cell_number = self.cleaned_data['cell_number']

        # Verifica que el nombre de usuario no esté en uso
        if Patient.objects.filter(cell_number=cell_number).exists():
            raise ValidationError('El nombre de usuario ya está en uso.')

        return cell_number
